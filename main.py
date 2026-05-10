import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


# Localizadores....

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
    close_payment_modal_button = (By.XPATH,"//div[contains(@class, 'payment-picker')]//button[contains(@class, 'section-close')]")
    comment_field = (By.ID, "comment")
    manta_switch = (By.XPATH,"//div[text()='Manta y pañuelos']/following-sibling::div")
    ice_cream_plus_button = (By.CSS_SELECTOR, ".counter-plus")
    order_taxi_final_button = (By.XPATH,"//button[contains(@class, 'smart-button')]")
    driver_modal_text = (By.CLASS_NAME,"order-header-title")



# Metodos......

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


    def set_phone_code(self, code):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.phone_code_field)
        ).send_keys(code)


    def click_next_phone_button(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.next_phone_button)
        ).click()


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


    def set_driver_message(self, message):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.comment_field)
        ).send_keys(message)


    def click_manta_switch(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.manta_switch)
        ).click()


    def click_ice_cream_plus_button(self, times):
        for i in range(times):
            WebDriverWait(self.driver, 5).until(
                expected_conditions.element_to_be_clickable(self.ice_cream_plus_button)
            ).click()


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


    # Tests ......

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        # cls.driver = webdriver.Chrome(desired_capabilities=capabilities)
        cls.driver = webdriver.Chrome()



    def test_set_route(self):
        self.driver.get(data.urban_routes_url)

        routes_page = UrbanRoutesPage(self.driver)

        address_from = data.address_from

        address_to = data.address_to

        routes_page.set_route(address_from, address_to)

        routes_page.click_order_taxi_button()

        routes_page.click_comfort_tariff()

        routes_page.click_phone_button()

        routes_page.set_phone_number(data.phone_number)

        routes_page.click_next_phone_button()

        code = retrieve_phone_code(self.driver)

        routes_page.set_phone_code(code)

        routes_page.click_confirm_phone_button()

        routes_page.click_payment_method_button()

        routes_page.click_add_card_button()

        routes_page.set_card_number(data.card_number)

        routes_page.set_card_code(data.card_code)

        routes_page.click_add_card_submit_button()

        routes_page.click_close_payment_modal_button()

        routes_page.set_driver_message(data.message_for_driver)

        routes_page.click_manta_switch()

        routes_page.click_ice_cream_plus_button(2)

        routes_page.click_order_taxi_final_button()


        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to
        assert "El conductor llegará" in routes_page.get_driver_modal_text()

    # Cierra la pagina al terminar de ejecutar las pruebas
    @classmethod
    def teardown_class(cls):
       cls.driver.quit()


    # metodo  para que no se cierre la pagina al terminar de ejecutar las pruebas durante el testing
    # def teardown_class(cls):
    # pass

