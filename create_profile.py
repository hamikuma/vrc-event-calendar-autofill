import os
import subprocess
import sys
import json
from pathlib import Path
from form_utils import (
    log_success, log_failure,
    fill_input_by_label, fill_textarea_by_label,
    select_option_by_label, click_button_by_text,
    fill_datetime_by_label, check_multiple_checkboxes_by_labels,
    wait_for_label, wait_for_form_section_change, select_radio_by_label
)


# ========================
# 設定ファイル（config.json）の読み込み
# ========================
script_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_dir, "config.json")

try:
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
        
except FileNotFoundError as e:
    log_failure(f"設定ファイルが見つかりません: {config_path}")
    exit(1)

# === プロファイル格納先の設定 ===
profile_dir = config["profile_path"]

# === ディレクトリが存在しなければ警告 ===
if not os.path.exists(profile_dir):
    log_failure(f"プロファイルディレクトリが見つかりません。作成してください。: {profile_dir}")
    sys.exit(1)

# === Chromeの実行ファイルを探す（一般的な2パターン）===
chrome_paths = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
]

chrome_exe = None
for path in chrome_paths:
    if os.path.exists(path):
        chrome_exe = path
        break

if not chrome_exe:
    log_failure("Chromeの実行ファイルが見つかりません。手動でパスを指定してください。")
    sys.exit(1)

# === Chrome起動コマンドの準備 ===
launch_cmd = [
    chrome_exe,
    f'--user-data-dir={profile_dir}',
    '--profile-directory=Default'
]

log_success(f"Chromeを以下の専用プロファイルで起動します:\n{profile_dir}")
log_success("➡ このChromeウィンドウで Google にログインし、完了後に閉じてください。\n")

# === Chromeを起動 ===
subprocess.Popen(launch_cmd)

# 待機させることでユーザーに説明を見せる
input("✅ Chromeが起動しました。ログインが完了したら Enter を押してください。")
log_success(f"プロファイルの作成が完了しました。Chromeブラウザを全て閉じてからautofill.pyを実行してください。")