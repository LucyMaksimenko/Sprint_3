from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import locators
import common_functions


class TestRegistration:
    def test_success_registration (self):
        driver = common_functions.start_browser()
        driver.find_element(By.XPATH, locators.sign_in_button).click()
        driver.find_element(By.XPATH, locators.register_button).click()
        driver.find_element(By.XPATH, locators.login_field_input).send_keys("Liudmila")
        driver.find_element(By.XPATH, locators.email_field_input).send_keys("liudmila_maksimenko_01_123@yandex.ru")
        driver.find_element(By.XPATH, locators.password_field_input).send_keys("123456789")
        driver.find_element(By.XPATH, locators.submit_register_button).click()
        assert driver.find_element(By.CSS_SELECTOR, locators.enter_to_profile_button_on_registration_page), "not found"

    def test_registration_with_invalid_password (self):
        driver = common_functions.start_browser()
        driver.find_element(By.XPATH, locators.sign_in_button).click()
        driver.find_element(By.XPATH, locators.register_button).click()
        driver.find_element(By.XPATH, locators.login_field_input).send_keys("Liudmila")
        driver.find_element(By.XPATH, locators.email_field_input).send_keys("liudmila_maksimenko_01_123@yandex.ru")
        driver.find_element(By.XPATH, locators.password_field_input).send_keys("123")
        driver.find_element(By.XPATH, locators.submit_register_button).click()
        text = driver.find_element(By.CSS_SELECTOR, locators.error_password_alert).text
        assert text == "Некорректный пароль"

    def test_registration_with_empty_name (self):
        driver = common_functions.start_browser()
        driver.find_element(By.XPATH, locators.sign_in_button).click()
        driver.find_element(By.XPATH, locators.register_button).click()
        driver.find_element(By.XPATH, locators.email_field_input).send_keys("liudmila_maksimenko_01_123@yandex.ru")
        driver.find_element(By.XPATH, locators.password_field_input).send_keys("123456789")
        driver.find_element(By.XPATH, locators.submit_register_button).click()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/register"

class TestLoginIn:

    def test_enter_to_account_button (self):
        driver = common_functions.start_browser()
        driver.find_element(By.XPATH, locators.sign_in_button).click()
        driver.find_element(By.CSS_SELECTOR, locators.email_login_field).send_keys("liudmila_maksimenko_01_123@yandex.ru")
        driver.find_element(By.CSS_SELECTOR, locators.password_login_field).send_keys("123456789")
        driver.find_element(By.CSS_SELECTOR, locators.log_in_button).click()
        driver.find_element(By.XPATH, locators.personal_account_button).click()
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH, locators.profile_button_in_menu)))
        assert driver.find_element(By.XPATH, locators.customer_name_in_profile), "customer_name_in_profile locator not found"


    def test_enter_with_personal_account_button (self):
        driver = common_functions.start_browser()
        driver.find_element(By.XPATH, locators.personal_account_button).click()
        driver.find_element(By.CSS_SELECTOR, locators.email_login_field).send_keys("liudmila_maksimenko_01_123@yandex.ru")
        driver.find_element(By.CSS_SELECTOR, locators.password_login_field).send_keys("123456789")
        driver.find_element(By.CSS_SELECTOR, locators.log_in_button).click()
        driver.find_element(By.XPATH, locators.personal_account_button).click()
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH, locators.profile_button_in_menu)))
        assert driver.find_element(By.XPATH, locators.customer_name_in_profile), "customer_name_in_profile locator not found"


    def test_enter_to_profile_from_registration_page (self):
        driver = common_functions.start_browser()
        driver.find_element(By.XPATH, locators.sign_in_button).click()
        driver.find_element(By.XPATH, locators.register_button).click()
        driver.find_element(By.CSS_SELECTOR, locators.enter_to_profile_button_on_registration_page).click()
        driver.find_element(By.CSS_SELECTOR, locators.email_login_field).send_keys("liudmila_maksimenko_01_123@yandex.ru")
        driver.find_element(By.CSS_SELECTOR, locators.password_login_field).send_keys("123456789")
        driver.find_element(By.CSS_SELECTOR, locators.log_in_button).click()
        driver.find_element(By.XPATH, locators.personal_account_button).click()
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH, locators.profile_button_in_menu)))
        assert driver.find_element(By.XPATH, locators.customer_name_in_profile), "customer_name_in_profile locator not found"


    def test_enter_from_restore_password_button(self):
        driver = common_functions.start_browser()
        driver.find_element(By.XPATH, locators.sign_in_button).click()
        driver.find_element(By.XPATH, locators.restore_password_button).click()
        driver.find_element(By.CSS_SELECTOR, locators.enter_to_profile_button_on_registration_page).click()
        driver.find_element(By.CSS_SELECTOR, locators.email_login_field).send_keys("liudmila_maksimenko_01_123@yandex.ru")
        driver.find_element(By.CSS_SELECTOR, locators.password_login_field).send_keys("123456789")
        driver.find_element(By.CSS_SELECTOR, locators.log_in_button).click()
        driver.find_element(By.XPATH, locators.personal_account_button).click()
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH, locators.profile_button_in_menu)))
        assert driver.find_element(By.XPATH, locators.customer_name_in_profile), "customer_name_in_profile locator not found"


    def test_exit_from_account(self):
        driver = common_functions.start_browser()
        driver.find_element(By.XPATH, locators.sign_in_button).click()
        driver.find_element(By.CSS_SELECTOR, locators.email_login_field).send_keys("liudmila_maksimenko_01_123@yandex.ru")
        driver.find_element(By.CSS_SELECTOR, locators.password_login_field).send_keys("123456789")
        driver.find_element(By.CSS_SELECTOR, locators.log_in_button).click()
        driver.find_element(By.XPATH, locators.personal_account_button).click()
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, locators.exit_button)))
        driver.find_element(By.CSS_SELECTOR, locators.exit_button).click()
        assert driver.find_element(By.CSS_SELECTOR, locators.log_in_button)

class TestNavigation:

    def test_from_personal_account_to_constructor_button(self):
        driver = common_functions.start_browser()
        driver.find_element(By.XPATH, locators.sign_in_button).click()
        driver.find_element(By.CSS_SELECTOR, locators.email_login_field).send_keys("liudmila_maksimenko_01_123@yandex.ru")
        driver.find_element(By.CSS_SELECTOR, locators.password_login_field).send_keys("123456789")
        driver.find_element(By.CSS_SELECTOR, locators.log_in_button).click()
        driver.find_element(By.XPATH, locators.personal_account_button).click()
        driver.find_element(By.XPATH, locators.constructor_button).click()
        assert driver.find_element(By.XPATH, locators.collect_burger_header)

    def test_from_personal_account_to_constructor_logo (self):
        driver = common_functions.start_browser()
        driver.find_element(By.XPATH, locators.sign_in_button).click()
        driver.find_element(By.CSS_SELECTOR, locators.email_login_field).send_keys("liudmila_maksimenko_01_123@yandex.ru")
        driver.find_element(By.CSS_SELECTOR, locators.password_login_field).send_keys("123456789")
        driver.find_element(By.CSS_SELECTOR, locators.log_in_button).click()
        driver.find_element(By.XPATH, locators.personal_account_button).click()
        driver.find_element(By.CSS_SELECTOR, locators.burger_logo).click()
        assert driver.find_element(By.XPATH, locators.collect_burger_header)

    def test_go_to_buns_section(self):
        driver = common_functions.start_browser()
        driver.find_element(By.XPATH, locators.sauses_section_in_constructor).click()
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, locators.buns_section_in_constructor)))
        driver.find_element(By.XPATH, locators.buns_section_in_constructor).click()
        assert WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH, locators.cards_with_buns)))

    def test_go_to_sauses_section(self):
        driver = common_functions.start_browser()
        driver.find_element(By.XPATH, locators.sauses_section_in_constructor).click()
        assert WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH, locators.cards_with_sauses)))

    def test_go_to_fillings_section(self):
        driver = common_functions.start_browser()
        driver.find_element(By.XPATH, locators.fillings_section_in_constructor).click()
        assert WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH, locators.cards_with_fillings)))
