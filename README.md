# 🎭 VRC Event Calendar Autofill

このスクリプトは、**VRC Event Calendar** の登録フォームに自動で定型文を入力するためのものです。pythonで動作し、Chromeブラウザを直接操作します。`config.json` に入力内容を記載して実行することで、手早くイベントを登録できます️。🚀

3/17更新 VRCイベントカレンダーの新フォームに対応しました。

---

## 📌 使い方
1. **pythonを導入**
2. **必要なライブラリをインストール**
   ```bash
   pip install selenium
   pip install webdriver-manager
   ```
3. **`config.json` を編集**
4. **スクリプトを実行**
   ```bash
   python autofill.py
   ```


---

## 📝 `config.json` の設定項目

`config.json` を編集して、Googleフォームに入力する内容を設定してください。
`config.json` に記載の内容を見たら見様見真似で分かると思いますが、以下に説明を載せておきます。

| **キー** | **内容** | **備考** |
|---------|---------|---------|
| `"profile_path"` | プロフィールパス | ブラウザのURL欄に"chrome://version/"と入力して、プロフィールパスに記載の内容を入力(User Data以降は不要。￥は/に置換する) |
| `"form_url"` | フォームURL | フォームのURL。変更不要 |
| `"event_name"` | イベント名 |  |
| `"android_support"` | Android対応可否 | `"PC"`, `"PC/android"`, `"android only"` のいずれか |
| `"start_date"` | 開始日付 | 空欄なら本日の日付が自動入力されます |
| `"start_hour"` | 開始時刻（時） | `00` ~ `23` |
| `"start_minute"` | 開始時刻（分） | `00` ~ `59` |
| `"end_date"` | 終了日付 | 空欄なら本日の日付が自動入力されます |
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