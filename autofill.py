import json
import os
import time
import signal
import sys
from datetime import datetime
import psutil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from form_utils import (
    log_success, log_failure,
    fill_input_by_label, fill_textarea_by_label,
    select_option_by_label, click_button_by_text,
    fill_datetime_by_label, check_multiple_checkboxes_by_labels,
    wait_for_label, wait_for_form_section_change, select_radio_by_label
)

# ========================
# Chromeが既に起動しているか確認する関数
# ========================
def is_chrome_running():
    for proc in psutil.process_iter(['name']):
        if "chrome" in proc.info['name'].lower():
            return True
    return False

# ========================
# WebDriverを安全に終了させる関数
# ========================
def cleanup(driver=None):
    try:
        if driver:
            driver.quit()
    except Exception as e:
        log_failure(f"WebDriver終了中にエラー: {e}")

# ========================
# 設定ファイル（config.json）の読み込み
# ========================
script_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_dir, "config.json")

try:
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
except FileNotFoundError as e:
    log_failure(f"設定ファイルが見つかりません: {config_path} {e}")
    exit(1)

# ========================
# Chromeが起動中なら警告を出して終了
# ========================
if is_chrome_running():
    log_failure(f"Chromeが既に起動しています。すべてのChromeを閉じてから再実行してください。")
    exit(1)

# ========================
# Chrome WebDriverのオプションを設定
# ========================
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=' + config["profile_path"])
options.add_argument('--profile-directory=Default')
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)
options.add_argument("--log-level=3")  # エラーだけ表示（INFO, WARNING, ERROR → 0〜3）
options.add_experimental_option("excludeSwitches", ["enable-logging"])  # DevToolsやConsoleログを抑制

# ========================
# WebDriverを起動
# ========================
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 2)

# ========================
# Googleフォームを開く
# ========================
driver.get(config["form_url"])

# ========================
# 本番処理：フォームの自動入力
# ========================

email_checkbox = wait.until(lambda d: d.find_element("xpath", "//div[@role='checkbox' and contains(@aria-label, '返信に表示するメールアドレス')]"))
time.sleep(0.5)
if config.get("record_the_email_address_to_reply"):
    if email_checkbox.get_attribute("aria-checked") != "true":
        email_checkbox.click()
        log_success("メールアドレスのチェックをONにしました")
else:
    if email_checkbox.get_attribute("aria-checked") == "true":
        email_checkbox.click()
        log_success("メールアドレスのチェックをOFFにしました")

fill_input_by_label(driver, wait, "イベント名", config["event_name"])
select_radio_by_label(driver, wait, "Android対応可否", config.get("android_support", "PC/android"))

start_date = config.get("start_date", "").strip() or datetime.today().strftime("%Y-%m-%d")
end_date = config.get("end_date", "").strip() or datetime.today().strftime("%Y-%m-%d")

fill_datetime_by_label(driver, wait, "開始日時", start_date, config["start_hour"], config["start_minute"])
fill_datetime_by_label(driver, wait, "終了日時", end_date, config["end_hour"], config["end_minute"])

select_option_by_label(driver, wait, "イベントを登録しますか", "イベントを登録する")

previous_section = driver.find_element("xpath", "//div[@role='list']")
click_button_by_text(driver, wait, "次へ")
wait_for_form_section_change(driver, previous_section)
wait_for_label(driver, "イベント主催者")

fill_input_by_label(driver, wait, "イベント主催者", config["event_host"])
fill_textarea_by_label(driver, wait, "イベント内容", config["event_content"])
check_multiple_checkboxes_by_labels(driver, wait, "イベントジャンル", config["genres"])
fill_textarea_by_label(driver, wait, "参加条件", config["participation_conditions"])
fill_textarea_by_label(driver, wait, "参加方法", config["participation_method"])
fill_textarea_by_label(driver, wait, "備考", config["remarks"])

if config.get("overseas_announcement"):
    select_option_by_label(driver, wait, "海外ユーザー向け告知", "希望する")

fill_textarea_by_label(driver, wait, "X告知文", config["x_announcement"])

log_success("自動入力完了。スクリプトを終了します（ブラウザはそのまま）。")
sys.exit()