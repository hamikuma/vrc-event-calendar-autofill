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

script_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_dir, "config.json")

try:
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
except FileNotFoundError:
    print(f"エラー: 設定ファイルが見つかりません: {config_path}")
    exit(1)

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def cleanup():
    try:
        driver.quit()
    except Exception:
        pass


driver.get(config["form_url"])
wait = WebDriverWait(driver, 15)

try:
    event_name_field = wait.until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='mG61Hd']/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input"))
    )
    event_name_field.clear()
    event_name_field.send_keys(config["event_name"])

    android_option = config.get("android_support", "PC/android")
    android_xpath = f"//span[contains(text(), '{android_option}')]"
    android_option_label = wait.until(EC.element_to_be_clickable((By.XPATH, android_xpath)))
    android_option_label.click()

    start_date = config.get("start_date", "").strip()
    if not start_date:
        start_date = datetime.today().strftime("%Y-%m-%d")

    date_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='date']")))
    date_field.send_keys(start_date)

    start_hour_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='mG61Hd']/div[2]/div[1]/div[2]/div[4]/div/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div[1]/input")))
    start_hour_field.send_keys(config["start_hour"])

    start_minute_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='mG61Hd']/div[2]/div[1]/div[2]/div[4]/div/div/div[2]/div/div[2]/div/div/div[3]/div/div[1]/div/div[1]/input")))
    start_minute_field.send_keys(config["start_minute"])

    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='mG61Hd']/div[2]/div[1]/div[3]/div[1]/div[1]/div")))
    next_button.click()

    event_host_field = wait.until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='mG61Hd']/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input"))
    )
    event_host_field.clear()
    event_host_field.send_keys(config["event_host"])

except Exception as e:
    print(f"エラーが発生しました: {e}")

time.sleep(10)
os.kill(driver.service.process.pid, signal.SIGTERM)
