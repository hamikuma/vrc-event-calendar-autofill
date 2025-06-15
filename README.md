# VRC Event Calendar Autofill

このスクリプトは、**VRC Event Calendar** のGoogleフォームに自動で定型文を入力します。
繰り返しの入力作業を省き、イベント運営を効率化できます🚀

---

## 🛠 構成ファイル
- `config.json` … 入力内容の設定ファイル
- `create_profile.exe` … メイン処理その1（Googleアカウントログインによるプロファイル作成）
- `autofill.exe` … メイン処理その2（Googleフォームを開き、情報自動入力）

## 📌 使い方
1. **Chromeブラウザをインストール**
2. **`vrc-event-calendar-autofill-v*.*.zip` をダウンロードし、解凍。→最新版(https://github.com/hamikuma/vrc-event-calendar-autofill/releases/latest)**
3. **`config.json` を編集してイベント内容を記入**
4. **`create_profile.exe`を実行して、Googleアカウントにログイン(ログイン情報の作成)**
5. **Chromeブラウザを全て閉じた状態で`autofill.exe`を実行**

---

## 📝 `config.json` の設定項目

`config.json` を編集して、VRCイベントカレンダーに入力する内容を設定してください。
`config.json` に既に記載している内容を参考に書き換えてください。以下詳細説明です。

| **キー** | **内容** | **備考** |
|---------|---------|---------|
| `"form_url"` | フォームURL | フォームのURL。変更不要 |
| `record_the_email_address_to_reply` | 返信に表示するメールアドレスとしてxxxを記録する | `true`で固定。変更不要 |
| `"event_name"` | イベント名 | 文字列 |
| `"android_support"` | Android対応可否 | `"PC"` / `"PC/android"` / `"android only"` |
| `start_date`, `end_date` | 開始・終了日 | 空欄にすると当日の日付が自動入力されます（YYYY-MM-DD） |
| `start_hour`, `start_minute` | 開始時刻 | 例：`"23"` / `"00"` |
| `end_hour`, `end_minute` | 終了時刻 | 例：`"23"` / `"59"` |
| `"event_host"` | イベント主催者 | |
| `"event_content"` | イベント内容 | |
| `"genres"` | イベントジャンル | 配列形式（例: `["音楽イベント", "交流会"]` |
| `"participation_conditions"` | 参加条件 | |
| `"participation_method"` | 参加方法 | |
| `"remarks"` | 備考 | |
| `"overseas_announcement"` | 海外向け告知 | `true` にすると選択される |
| `"x_announcement"` | X告知文 | |

---
## ❌ 注意
※1 profile_pathはChromeのデフォルトパス(例：C:\Users\CurrentUser\AppData\Local\Google\Chrome\User Data)を指定するとエラーとなるので、別の保存先を用意してください。

## 🎥 デモ動画
https://github.com/user-attachments/assets/6c973090-cc8b-4ba0-9659-d0e73a78031e

## 🧑‍💻 更新履歴
- 2025/6/15 profileを、config.jsonで指定ではなく実行フォルダ配下で生成する仕様に変更
- 2025/5/16 パッケージ化

=======

- ご要望・不明点・改善点などあれば気軽にご連絡ください！もしくはIssueの作成やPull Requestをぜひお願いします 🙌
