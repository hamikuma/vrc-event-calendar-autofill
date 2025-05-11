# 🎭 VRC Event Calendar Autofill

このスクリプトは、**VRC Event Calendar** のGoogleフォームに自動で定型文を入力します。
繰り返しの入力作業を省き、イベント運営を効率化できます🚀

---

## 🛠 構成ファイル

- `create_profile.py` … メイン処理その1（Googleアカウントの事前ログイン処理）
- `autofill.py` … メイン処理その2（Googleフォームを開き、情報を入力）
- `form_utils.py` … 入力・選択などの共通処理をまとめた関数群
- `config.json` … 入力内容の設定ファイル
- `requirements.txt` … 必要なPythonライブラリの一覧

## 📌 使い方
1. **Chromeブラウザ、pythonをインストール（バージョン3.8以上推奨）**
2. **python実行環境でこのモジュールをクローン**
   ```bash
   git clone https://github.com/hamikuma/vrc-event-calendar-autofill.git
   ```
3. **必要なライブラリをインストール**
   ```bash
   pip install -r requirements.txt
   ```
4. **`config.json` を編集してイベント内容を記入**
5. **`create_profile.py`を実行して、Googleアカウントにログイン(ログイン情報の作成)**
   ```bash
   python create_profile.py
   ```
6. **Chromeブラウザを全て閉じた状態で`autofill.py`を実行**
   ```bash
   python autofill.py
   ```


---

## 📝 `config.json` の設定項目

`config.json` を編集して、Googleフォームに入力する内容を設定してください。
`config.json` に記載の内容を見たら見様見真似で分かると思いますが、以下に説明を載せておきます。

| **キー** | **内容** | **備考** |
|---------|---------|---------|
| `"profile_path"` | ログイン情報の保存先ディレクトリ | 任意のディレクトリを作成して、指定してください。(Chromeのデフォルトパス(~/User Data)を指定するとエラーとなる。￥は/に置換する) |
| `"form_url"` | フォームURL | フォームのURL。変更不要 |
| `record_the_email_address_to_reply` | 返信に表示するメールアドレスとしてxxxを記録する | `true`で固定 |
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

## ✅ 補足事項

- **Googleにログイン済みのChromeプロファイル**を使用する必要があります。
- スクリプトは**Chromeが起動していない状態**でのみ実行可能です。
- 入力が完了すると、ブラウザは開いたまま終了します。

---

## 📦 依存ライブラリ（requirements.txt）

```
selenium
webdriver-manager
psutil
```

---
## 🎥 デモ動画

https://github.com/user-attachments/assets/9ff533b1-1379-400f-ab65-2a4ad248d30e

## 🧑‍💻 更新履歴
- 2025/5/11 Chromeのセキュリティアップデートで動かなくなっていたので違う方法に変更
- 2025/4/6　デモ動画を掲載
- 2025/3/17　新フォームに対応
- 2025/3/24　バグ修正、実行ログが表示されるように修正

=======

- ご要望・不明点・改善点などあれば気軽にご連絡ください！もしくはIssueの作成やPull Requestをぜひお願いします 🙌
