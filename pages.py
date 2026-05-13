from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    comfort_tariff = (By.XPATH, "//div[text()='Comfort']")
    order_taxi_button = (By.XPATH, "//button[text()='Pedir un taxi']")
    phone_button = (By.CLASS_NAME, "np-text")
    phone_input = (By.ID, "phone")
    next_phone_button = (By.XPATH, "//button[text()='Siguiente']")
    phone_code_field = (By.ID, "code")
    confirm_phone_button = (By.XPATH, "//button[text()='Confirmar']")

    payment_method_button = (By.XPATH, "//div[contains(@class, 'pp-button') and .//div[text()='Método de pago']]")
    add_card_button = (By.XPATH, "//div[text()='Agregar tarjeta']")
    card_number_field = (By.ID, "number")
    card_code_field = (By.XPATH, "//div[@class='card-code-input']//input[@id='code']")
    add_card_submit_button = (By.XPATH, "//button[text()='Agregar']")
    close_payment_modal_button = (By.XPATH, "//div[contains(@class, 'payment-picker')]//button[contains(@class, 'section-close')]")

    comment_field = (By.ID, "comment")
    manta_switch = (By.XPATH, "//div[text()='Manta y pañuelos']/following-sibling::div")
    ice_cream_plus_button = (By.CSS_SELECTOR, ".counter-plus")
    ice_cream_counter = (By.XPATH, "//div[text()='Helado']/following-sibling::div//div[contains(@class,'counter-value')]")

    order_taxi_final_button = (By.XPATH, "//button[contains(@class, 'smart-button')]")
    driver_modal_text = (By.CLASS_NAME, "order-header-title")

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.from_field)
        ).send_keys(from_address)

    def set_to(self, to_address):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.to_field)
        ).send_keys(to_address)

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def click_comfort_tariff(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.comfort_tariff)
        ).click()

    def get_comfort_tariff_text(self):
        return self.driver.find_element(*self.comfort_tariff).text

    def click_order_taxi_button(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.order_taxi_button)
        ).click()

    def click_phone_button(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.phone_button)
        ).click()

    def set_phone_number(self, phone_number):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.phone_input)
        ).send_keys(phone_number)

    def get_phone_number(self):
        return self.driver.find_element(*self.phone_button).text

    def click_next_phone_button(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.next_phone_button)
        ).click()

    def set_phone_code(self, code):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.phone_code_field)
        ).send_keys(code)

    def click_confirm_phone_button(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.confirm_phone_button)
        ).click()

    def click_payment_method_button(self):
        payment_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.payment_method_button)
        )
        self.driver.execute_script("arguments[0].click();", payment_button)

    def click_add_card_button(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.add_card_button)
        ).click()

    def set_card_number(self, card_number):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.card_number_field)
        ).send_keys(card_number)

    def set_card_code(self, card_code):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.card_code_field)
        ).send_keys(card_code, Keys.TAB)

    def click_add_card_submit_button(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.add_card_submit_button)
        ).click()

    def click_close_payment_modal_button(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.close_payment_modal_button)
        ).click()

    def get_payment_method_text(self):
        return self.driver.find_element(*self.payment_method_button).text

    def set_driver_message(self, message):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.comment_field)
        ).send_keys(message)

    def get_driver_message(self):
        return self.driver.find_element(*self.comment_field).get_property('value')

    def click_manta_switch(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.manta_switch)
        ).click()

    def is_manta_switch_displayed(self):
        return self.driver.find_element(*self.manta_switch).is_displayed()

    def get_manta_switch_class(self):
        return self.driver.find_element(*self.manta_switch).get_attribute("class")

    def click_ice_cream_plus_button(self, times):
        for i in range(times):
            WebDriverWait(self.driver, 5).until(
                expected_conditions.element_to_be_clickable(self.ice_cream_plus_button)
            ).click()

    def get_ice_cream_counter(self):
        return self.driver.find_element(*self.ice_cream_counter).text

    def click_order_taxi_final_button(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.order_taxi_final_button)
        ).click()

    def get_driver_modal_text(self):
        WebDriverWait(self.driver, 40).until(
            expected_conditions.text_to_be_present_in_element(
                self.driver_modal_text,
                "El conductor llegará"
            )
        )
        return self.driver.find_element(*self.driver_modal_text).text