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
    wait_for_label, wait_for_form_section_change, select_radio_by_label, get_config_path
)


# ========================
# 設定ファイル（config.json）の読み込み
# ========================
config_path = get_config_path()

try:
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
        
except FileNotFoundError as e:
    log_failure(f"設定ファイルが見つかりません: {config_path}")
    input("終了します。Enterキーを押してください")
    sys.exit(1)

# === プロファイル格納先の設定 ===
if getattr(sys, 'frozen', False):
    profile_dir = os.path.dirname(sys.executable) + "\profile"
else:
    profile_dir = os.path.dirname(os.path.abspath(__file__)) + "\profile"

# === ディレクトリが存在しなければ警告 ===
if not os.path.exists(profile_dir):
    log_failure(f"プロファイルディレクトリが見つかりません。作成してください。: {profile_dir}")
    input("終了します。Enterキーを押してください")
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
    input("終了します。Enterキーを押してください")
    sys.exit(1)

# === Chrome起動コマンドの準備 ===
launch_cmd = [
    chrome_exe,
    f'--user-data-dir={profile_dir}',
    '--profile-directory=Default'
]

log_success(f"Googleログインを実施いただき以下に専用プロファイルを作成します。:\n{profile_dir}")

# === Chromeを起動 ===
subprocess.Popen(launch_cmd)

# 待機させることでユーザーに説明を見せる
log_success(f"Chromeが起動しました。")
input("Googleログインが完了したらEnterキーを押してください。その後、autofill.exeを実行してください。")
sys.exit(1)