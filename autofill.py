import json
import os
import time
import signal
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# ✅ スクリプトのあるフォルダから `config.json` を読み込む
script_dir = os.path.dirname(os.path.abspath(__file__))  # 実行ファイルのディレクトリを取得
config_path = os.path.join(script_dir, "config.json")  # `config.json` の絶対パスを取得

# 設定ファイルを読み込む
try:
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
except FileNotFoundError:
    print(f"エラー: 設定ファイルが見つかりません: {config_path}")
    exit(1)

# ✅ ユーザープロファイルを正しく指定
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=' + config["profile_path"])  # プロファイルデータのフォルダ
options.add_argument('--profile-directory=Default')  # 使用するプロファイル

# ✅ Chrome WebDriverのセットアップ
options.add_argument("--start-maximized")  # ウィンドウを最大化
options.add_experimental_option("detach", True)  # ブラウザを閉じない
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)



# ✅ プログラム終了時に Selenium を安全に開放（バックグラウンドプロセスを解放）
def cleanup():
    try:
        driver.quit()  # ✅ WebDriverのプロセスを解放
    except Exception:
        pass

# ✅ フォームを開く
driver.get(config["form_url"])

try:
    wait = WebDriverWait(driver, 10)  # 最大10秒待機

    # イベント名
    event_name_field = wait.until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='mG61Hd']/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input"))
    )
    event_name_field.clear()
    event_name_field.send_keys(config["event_name"])

    # Android対応可否（ラジオボタンを選択）
    android_option = config.get("android_support", "PC/android")
    android_xpath = f"//span[contains(text(), '{android_option}')]"
    android_option_label = wait.until(EC.element_to_be_clickable((By.XPATH, android_xpath)))
    android_option_label.click()

    # ✅ `start_date` の処理
    start_date = config.get("start_date", "").strip()  # 空白削除
    if not start_date:  # 空欄の場合は本日の日付を使用
        start_date = datetime.today().strftime("%Y-%m-%d")

    # ✅ 開始日付（config.json に event_date の指定がある場合はそれを使用、なければ本日の日付）
    date_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='date']")))
    date_field.send_keys(start_date)

    # ✅ 開始時刻（時・分）
    start_hour_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='mG61Hd']/div[2]/div[1]/div[2]/div[4]/div/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div[1]/input")))
    start_hour_field.send_keys(config["start_hour"])

    start_minute_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='mG61Hd']/div[2]/div[1]/div[2]/div[4]/div/div/div[2]/div/div[2]/div/div/div[3]/div/div[1]/div/div[1]/input")))
    start_minute_field.send_keys(config["start_minute"])

    # ✅ `end_date` の処理
    end_date = config.get("end_date", "").strip()  # 空白削除
    if not end_date:  # 空欄の場合は本日の日付を使用
        end_date = datetime.today().strftime("%Y-%m-%d")

    # ✅ 終了日付（config.json に end_date の指定がある場合はそれを使用、なければ本日の日付）
    date_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='mG61Hd']/div[2]/div[1]/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input")))
    date_field.send_keys(end_date)

    # ✅ 終了時刻（時・分）
    end_hour_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='mG61Hd']/div[2]/div[1]/div[2]/div[5]/div/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div[1]/input")))
    end_hour_field.send_keys(config["end_hour"])

    end_minute_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='mG61Hd']/div[2]/div[1]/div[2]/div[5]/div/div/div[2]/div/div[2]/div/div/div[3]/div/div[1]/div/div[1]/input")))
    end_minute_field.send_keys(config["end_minute"])
    
    # 登録するを選択
    event_register_button = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='mG61Hd']/div[2]/div[1]/div[2]/div[6]/div/div/div[2]/div/div[1]/div[1]/div[3]/span")))
    event_register_button.click()

    # ✅ 「次へ」をクリック
    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='mG61Hd']/div[2]/div[1]/div[3]/div[1]/div[1]/div")))
    next_button.click()


    # ✅ 2ページ目のロードを待機（イベント主催者欄がロードされるまで）
    event_host_field = wait.until(EC.presence_of_element_located(((By.XPATH, "//*[@id='mG61Hd']/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input"))))

    # ✅ イベント主催者
    event_host_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='mG61Hd']/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")))
    event_host_field.clear()
    event_host_field.send_keys(config["event_host"])

    # ✅ イベント内容
    event_content_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='mG61Hd']/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea")))
    event_content_field.clear()
    event_content_field.send_keys(config["event_content"])

    # ✅ イベントジャンル（複数選択）
    target_labels = config["genres"]
    checkboxes = driver.find_elements(By.XPATH, "//label")
    for checkbox in checkboxes:
        label_text = checkbox.text.strip()
        if label_text in target_labels:
            if not checkbox.is_selected():
                checkbox.click()
            time.sleep(1)

    # ✅ 参加条件
    participation_conditions_field = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/form/div[2]/div[1]/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/textarea")))
    participation_conditions_field.clear()
    participation_conditions_field.send_keys(config["participation_conditions"])

    # ✅ 参加方法
    participation_method_field = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/form/div[2]/div[1]/div[2]/div[6]/div/div/div[2]/div/div[1]/div[2]/textarea")))
    participation_method_field.clear()
    participation_method_field.send_keys(config["participation_method"])

    # ✅ 備考
    remarks_field = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/form/div[2]/div[1]/div[2]/div[7]/div/div/div[2]/div/div[1]/div[2]/textarea")))
    remarks_field.clear()
    remarks_field.send_keys(config["remarks"])

    # ✅ 海外ユーザー向け告知（チェックボックス）
    if config["overseas_announcement"]:
        overseas_checkbox = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='mG61Hd']/div[2]/div[1]/div[2]/div[8]/div/div/div[2]/div/div[1]/div[1]/div[3]/span")))
        overseas_checkbox.click()

    # ✅ X告知文
    x_announcement_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='mG61Hd']/div[2]/div[1]/div[2]/div[9]/div/div/div[2]/div/div[1]/div[2]/textarea")))
    x_announcement_field.clear()
    x_announcement_field.send_keys(config["x_announcement"])

#     # 送信ボタンをクリック
#     submit_button = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='mG61Hd']/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/span/span"))
#     #送信まで自動化するなら正しく入力されているか一度確認の上、コメントアウトを外す
#     #submit_button.click()

except Exception as e:
    print(f"エラーが発生しました: {e}")


#処理を終了する
time.sleep(10)
os.kill(driver.service.process.pid, signal.SIGTERM)