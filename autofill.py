import json
import os
import time
import signal
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time

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

# ✅ `event_date` の処理
event_date = config.get("event_date", "").strip()  # 空白削除
if not event_date:  # 空欄の場合は本日の日付を使用
    event_date = datetime.today().strftime("%Y-%m-%d")

# Chrome WebDriverのセットアップ
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # ウィンドウを最大化
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

# ✅ プログラム終了時に Selenium を安全に開放（バックグラウンドプロセスを解放）
def cleanup():
    try:
        driver.quit()  # ✅ これで TensorFlow Lite のプロセスも解放される
    except Exception:
        pass

# フォームを開く
driver.get(config["form_url"])

# ✅ ページが完全にロードされるまで待機
wait = WebDriverWait(driver, 15)  # 最大15秒待機
email_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))


try:
    wait = WebDriverWait(driver, 10)  # 最大10秒待機

    # メールアドレス
    email_field = driver.find_element(By.XPATH, "//input[@type='email']")
    email_field.send_keys(config["email"])

    # イベント名
    event_name_field = driver.find_element(By.XPATH, "//input[@type='text']")
    event_name_field.send_keys(config["event_name"])

    # Android対応可否（ラジオボタンを選択）
    android_option = config.get("android_support", "PC/Android両対応")
    android_xpath = f"//span[contains(text(), '{android_option}')]"
    android_option_label = driver.find_element(By.XPATH, android_xpath)
    android_option_label.click()

    # ✅ 日付の設定（config.json に event_date がある場合はそれを使用、なければ本日の日付）
    date_field = driver.find_element(By.XPATH, "//input[@type='date']")
    date_field.send_keys(event_date)

    # ✅ 開始時刻（時・分）
    start_hour_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='mG61Hd']/div[2]/div[1]/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input")))
    start_hour_field.send_keys(config["start_hour"])

    start_minute_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='mG61Hd']/div[2]/div[1]/div[2]/div[5]/div/div/div[2]/div/div[3]/div/div[1]/div/div[1]/input")))
    start_minute_field.send_keys(config["start_minute"])

    # ✅ 終了時刻（時・分）
    end_hour_field = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div[1]/div[2]/div[6]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input")
    end_hour_field.send_keys(config["end_hour"])

    end_minute_field = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div[1]/div[2]/div[6]/div/div/div[2]/div/div[3]/div/div[1]/div/div[1]/input")
    end_minute_field.send_keys(config["end_minute"])

    # ✅ 「次へ」ボタンがクリック可能になるまで待機
    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), '次へ')]")))
    next_button.click()

    # ✅ 2ページ目のロードを待機（イベント主催者欄がロードされるまで）
    event_host_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='mG61Hd']/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")))

    # ✅ イベント主催者
    event_host_field = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    event_host_field.send_keys(config["event_host"])

    # ✅ イベント内容
    event_content_field = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div[1]/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea")
    event_content_field.send_keys(config["event_content"])

    # ✅ イベントジャンル（複数選択）
    for genre in config["genres"]:
        genre_checkbox = driver.find_element(By.XPATH, f"//span[contains(text(), '{genre}')]")
        genre_checkbox.click()

    # ✅ 参加条件
    participation_conditions_field = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div[1]/div[2]/div[6]/div/div/div[2]/div/div[1]/div[2]/textarea")
    participation_conditions_field.send_keys(config["participation_conditions"])

    # ✅ 参加方法
    participation_method_field = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div[1]/div[2]/div[7]/div/div/div[2]/div/div[1]/div[2]/textarea")
    participation_method_field.send_keys(config["participation_method"])

    # ✅ 備考
    remarks_field = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div[1]/div[2]/div[8]/div/div/div[2]/div/div[1]/div[2]/textarea")
    remarks_field.send_keys(config["remarks"])

    # ✅ X告知文
    x_announcement_field = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div[1]/div[2]/div[10]/div/div/div[2]/div/div[1]/div[2]/textarea")
    x_announcement_field.send_keys(config["x_announcement"])

    # ✅ 海外ユーザー向け告知（チェックボックス）
    if config["overseas_announcement"]:
        overseas_checkbox = driver.find_element(By.XPATH, "//*[@id='i72']")
        overseas_checkbox.click()


    # 送信ボタンをクリック
    submit_button = driver.find_element(By.XPATH, "//span[contains(text(), '送信')]")
    #送信まで自動化するなら動作確認の上、コメントアウトを外す
    #submit_button.click()



except Exception as e:
    print(f"エラーが発生しました: {e}")


#処理を終了する
time.sleep(10)
os.kill(driver.service.process.pid,signal.SIGTERM)

#ブラウザを閉じる場合
#driver.quit()