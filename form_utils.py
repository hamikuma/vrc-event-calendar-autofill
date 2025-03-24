from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ========================
# ログ出力関数
# ========================
def log_success(message):
    print(f"✅ {message}")

def log_failure(message):
    print(f"⚠ {message}")

# ========================
# 共通操作関数
# ========================
def fill_input_by_label(driver, wait, label_text, value):
    try:
        input_elem = wait.until(EC.presence_of_element_located((
            By.XPATH, f"//span[contains(text(), '{label_text}')]/ancestor::div[contains(@class, 'HoXoMd')]/following::input[@type='text'][1]"
        )))
        input_elem.clear()
        input_elem.send_keys(value)
        log_success(f"「{label_text}」に入力が完了しました")
    except Exception as e:
        log_failure(f"「{label_text}」の入力に失敗しました: {e}")

def fill_textarea_by_label(driver, wait, label_text, value):
    try:
        textarea_elem = wait.until(EC.presence_of_element_located((
            By.XPATH, f"//span[contains(text(), '{label_text}')]/ancestor::div[contains(@class, 'HoXoMd')]/following::textarea[1]"
        )))
        textarea_elem.clear()
        textarea_elem.send_keys(value)
        log_success(f"「{label_text}」のテキストエリアに入力が完了しました")
    except Exception as e:
        log_failure(f"「{label_text}」のテキストエリア入力に失敗しました: {e}")

def select_option_by_label(driver, wait, label_text, option_text):
    try:
        label_elem = wait.until(EC.presence_of_element_located((
            By.XPATH, f"//span[contains(text(), '{label_text}')]"
        )))
        container = label_elem.find_element(By.XPATH, "./ancestor::div[contains(@class, 'Qr7Oae')]")
        dropdown = container.find_element(By.XPATH, ".//div[@role='listbox']")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", dropdown)
        time.sleep(0.5)
        dropdown.click()
        time.sleep(1)
        option_elem = wait.until(EC.element_to_be_clickable((
            By.XPATH, f"//div[@role='option'][.//span[contains(text(), '{option_text}')]]"
        )))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", option_elem)
        option_elem.click()
        time.sleep(0.5)
        log_success(f"「{label_text}」に「{option_text}」を選択しました")
    except Exception as e:
        log_failure(f"「{label_text}」の選択に失敗しました: {e}")

def click_button_by_text(driver, wait, button_text):
    try:
        button = wait.until(EC.presence_of_element_located((
            By.XPATH, f"//div[@role='button' and .//span[text()='{button_text}']]"
        )))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        time.sleep(0.5)
        try:
            WebDriverWait(driver, 1).until(
                EC.invisibility_of_element_located((By.CLASS_NAME, "ThHDze"))
            )
        except:
            pass
        WebDriverWait(driver, 1).until(EC.element_to_be_clickable((
            By.XPATH, f"//div[@role='button' and .//span[text()='{button_text}']]"
        ))).click()
        log_success(f"「{button_text}」ボタンをクリックしました")
    except Exception as e:
        log_failure(f"「{button_text}」ボタンのクリックに失敗しました: {e}")

def fill_datetime_by_label(driver, wait, label_text, date_str, hour_str, minute_str):
    try:
        label_elem = wait.until(EC.presence_of_element_located((
            By.XPATH, f"//span[contains(text(), '{label_text}')]"
        )))
        container = label_elem.find_element(By.XPATH, "./ancestor::div[contains(@class, 'Qr7Oae')]")
        date_input = container.find_element(By.XPATH, ".//input[@type='date']")
        hour_input = container.find_element(By.XPATH, ".//input[@type='text' and @aria-label='時']")
        minute_input = container.find_element(By.XPATH, ".//input[@type='text' and @aria-label='分']")

        date_input.clear()
        date_input.send_keys(date_str)
        hour_input.clear()
        hour_input.send_keys(hour_str)
        minute_input.clear()
        minute_input.send_keys(minute_str)

        log_success(f"「{label_text}」の日時入力が完了しました")
    except Exception as e:
        log_failure(f"「{label_text}」の日時入力に失敗しました: {e}")

def check_multiple_checkboxes_by_labels(driver, wait, label_text, target_labels):
    try:
        # ラベル要素の検索修正
        label_elem = wait.until(EC.presence_of_element_located((
            By.XPATH, f"//div[contains(@class, 'HoXoMd') and .//span[contains(text(), '{label_text}')]]"
        )))
        container = label_elem.find_element(By.XPATH, "./ancestor::div[contains(@class, 'Qr7Oae')]")

        # チェックボックス取得
        checkbox_labels = container.find_elements(By.XPATH, ".//*[@role='checkbox']")

        for checkbox in checkbox_labels:
            label = checkbox.get_attribute("aria-label") or checkbox.text.strip()
            is_checked = checkbox.get_attribute("aria-checked") == "true"

            if label in target_labels and not is_checked:
                checkbox.click()
                log_success(f"「{label_text}」の「{label}」にチェックを入れました")
            elif label in target_labels and is_checked:
                log_success(f"「{label_text}」の「{label}」は既にチェックされています")
            elif label not in target_labels and is_checked:
                checkbox.click()
                log_success(f"「{label_text}」の「{label}」のチェックを外しました")
    except Exception as e:
        log_failure(f"「{label_text}」の複数選択チェックに失敗しました: {e}")

def select_radio_by_label(driver, wait, label_text, option_text):
    try:
        # ラベル要素取得
        label_elem = wait.until(EC.presence_of_element_located((
            By.XPATH, f"//*[contains(text(), '{label_text}')]"
        )))
        container = label_elem.find_element(By.XPATH, "./ancestor::div[contains(@class, 'Qr7Oae')]")

        # aria-label で完全一致するラジオボタンを検索
        radio = container.find_element(By.XPATH, f".//*[@role='radio' and @aria-label='{option_text}']")

        # スクロールしてクリック
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", radio)
        time.sleep(0.5)
        if radio.get_attribute("aria-checked") != "true":
            radio.click()
            log_success(f"「{label_text}」で「{option_text}」を選択しました")
        else:
            log_success(f"「{label_text}」の「{option_text}」は既に選択されています")
    except Exception as e:
        log_failure(f"「{label_text}」のラジオボタン選択に失敗しました: {e}")

def wait_for_label(driver, label_text, timeout=10):
    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, f"//span[contains(text(), '{label_text}')]"))
        )
        log_success(f"「{label_text}」が表示されました（ページ遷移完了）")
    except Exception as e:
        log_failure(f"「{label_text}」の表示待ちに失敗: {e}")
        raise

def wait_for_form_section_change(driver, previous_section):
    try:
        WebDriverWait(driver, 10).until(
            lambda d: d.find_element(By.XPATH, "//div[@role='list']") != previous_section
        )
    except Exception as e:
        log_failure(f"セクション切り替え待ちに失敗: {e}")
        raise
