# 🎭 VRC Event Calendar Autofill

このスクリプトは、**VRC Event Calendar** の登録フォームに自動で定型文を入力するためのものです。pythonで動作します。
`config.json` を編集することで、誰でも簡単にイベントを登録できます️。🚀

---

## 📌 使い方
1. **pythonを導入**
2. **Chromeブラウザのバージョンを確認**  
3. **対応する ChromeDriver を取得**  
   - [ChromeDriver ダウンロードページ](https://googlechromelabs.github.io/chrome-for-testing/) から、**お使いのChromeと同じバージョン**の `chromedriver.exe` をダウンロード。
4. **`chromedriver.exe` を Pythonの実行ファイルと同じフォルダに配置**
5. **必要なライブラリをインストール**
   pip install selenium
6. **`config.json` を編集**
7. **スクリプトを実行**
   python autofill.py

---

## 📝 `config.json` の設定項目

`config.json` を編集して、Googleフォームに入力する内容を設定してください。

| **キー** | **内容** | **備考** |
|---------|---------|---------|
| `"email"` | メールアドレス |  |
| `"event_name"` | イベント名 |  |
| `"android_support"` | Android対応可否 | `"PCオンリー"`, `"PC/Android両対応"`, `"Android オンリー"` のいずれか |
| `"event_date"` | 日付 | 空欄なら本日の日付が自動入力されます |
| `"start_hour"` | 開始時刻（時） | `00` ~ `23` |
| `"start_minute"` | 開始時刻（分） | `00` ~ `59` |
| `"end_hour"` | 終了時刻（時） | `00` ~ `23` |
| `"end_minute"` | 終了時刻（分） | `00` ~ `59` |
| `"event_host"` | イベント主催者 | |
| `"event_content"` | イベント内容 | |
| `"genres"` | イベントジャンル | 配列形式（例: `["音楽イベント", "交流会"]` |
| `"participation_conditions"` | 参加条件 | |
| `"participation_method"` | 参加方法 | |
| `"remarks"` | 備考 | |
| `"overseas_announcement"` | 海外向け告知 | `true` でチェックON、`false` でチェックOFF |
| `"x_announcement"` | X告知文 | |

---

## ⚠️ **注意点**
- **最終送信ボタン (`送信` のクリック処理) は安全のためコメントアウト** しています。  
  - 自動送信を有効にする場合は直前までの動作確認の上、 `autofill.py` 内の `submit_button.click()` のコメントを解除してください。

---

## 📚 **関連リンク**
- **ChromeDriver ダウンロードページ**: [公式サイト](https://sites.google.com/chromium.org/driver/)
- **Python Selenium の公式ドキュメント**: [Selenium Python Bindings](https://www.selenium.dev/documentation/webdriver/)

