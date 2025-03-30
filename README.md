# 🎭 VRC Event Calendar Autofill

このスクリプトは、**VRC Event Calendar** のGoogleフォームに自動で定型文を入力します。
繰り返しの入力作業を省き、イベント運営を効率化できます🚀

---

## 🛠 構成ファイル

- `autofill.py` … メイン処理（Googleフォームを開き、情報を入力）
- `form_utils.py` … 入力・選択などの共通処理をまとめた関数群
- `config.json` … 入力内容の設定ファイル
- `requirements.txt` … 必要なPythonライブラリの一覧

## 📌 使い方
1. **Chromeブラウザ、pythonをインストール（バージョン3.8以上推奨）**
2. **必要なライブラリをインストール**
   ```bash
   pip install -r requirements.txt
   ```
3. **`config.json` を編集してイベント内容を記入**
4. **ChromeブラウザでGoogleアカウントにログイン済であることを確認する**
5. **Chromeブラウザを全て閉じた状態でスクリプトを実行**
   ```bash
   python autofill.py
   ```


---

## 📝 `config.json` の設定項目

`config.json` を編集して、Googleフォームに入力する内容を設定してください。
`config.json` に記載の内容を見たら見様見真似で分かると思いますが、以下に説明を載せておきます。

| **キー** | **内容** | **備考** |
|---------|---------|---------|
| `"profile_path"` | Chromeのプロファイルパス | ブラウザのURL欄に"chrome://version/"と入力して、プロフィールパスに記載の内容を入力(User Data以降は不要。￥は/に置換する) |
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

## 🧑‍💻 作者メモ

- 2024/3/17　新フォームに対応
- 2024/3/24　バグ修正、実行ログが表示されるように修正
<<<<<<< HEAD
- ご要望・不明点・改善点などあれば気軽にご連絡ください！
=======
- ご要望・不明点・改善点などあれば気軽にご連絡ください！
