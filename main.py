import data
from selenium import webdriver
from pages import UrbanRoutesPage
from helpers import retrieve_phone_code


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

    def open_page(self):
        self.driver.get(data.urban_routes_url)
        return UrbanRoutesPage(self.driver)

    def prepare_route(self):
        routes_page = self.open_page()
        routes_page.set_route(data.address_from, data.address_to)
        routes_page.click_order_taxi_button()
        return routes_page

    def prepare_phone_confirmed(self):
        routes_page = self.prepare_route()
        routes_page.click_comfort_tariff()
        routes_page.click_phone_button()
        routes_page.set_phone_number(data.phone_number)
        routes_page.click_next_phone_button()
        code = retrieve_phone_code(self.driver)
        routes_page.set_phone_code(code)
        routes_page.click_confirm_phone_button()
        return routes_page

    def prepare_card_added(self):
        routes_page = self.prepare_phone_confirmed()
        routes_page.click_payment_method_button()
        routes_page.click_add_card_button()
        routes_page.set_card_number(data.card_number)
        routes_page.set_card_code(data.card_code)
        routes_page.click_add_card_submit_button()
        routes_page.click_close_payment_modal_button()
        return routes_page

    def prepare_order_ready(self):
        routes_page = self.prepare_card_added()
        routes_page.set_driver_message(data.message_for_driver)
        routes_page.click_manta_switch()
        routes_page.click_ice_cream_plus_button(2)
        return routes_page

    def test_set_route(self):
        routes_page = self.open_page()

        routes_page.set_route(data.address_from, data.address_to)

        assert routes_page.get_from() == data.address_from
        assert routes_page.get_to() == data.address_to

    def test_select_comfort_tariff(self):
        routes_page = self.prepare_route()

        routes_page.click_comfort_tariff()

        assert routes_page.get_comfort_tariff_text() == "Comfort"

    def test_add_phone_number(self):
        routes_page = self.prepare_route()

        routes_page.click_phone_button()
        routes_page.set_phone_number(data.phone_number)

        assert routes_page.driver.find_element(*routes_page.phone_input).get_property("value") == data.phone_number

    def test_confirm_phone_code(self):
        routes_page = self.prepare_route()

        routes_page.click_phone_button()
        routes_page.set_phone_number(data.phone_number)
        routes_page.click_next_phone_button()
        code = retrieve_phone_code(self.driver)
        routes_page.set_phone_code(code)
        routes_page.click_confirm_phone_button()

        assert data.phone_number in routes_page.get_phone_number()

    def test_add_card(self):
        routes_page = self.prepare_phone_confirmed()

        routes_page.click_payment_method_button()
        routes_page.click_add_card_button()
        routes_page.set_card_number(data.card_number)
        routes_page.set_card_code(data.card_code)
        routes_page.click_add_card_submit_button()
        routes_page.click_close_payment_modal_button()

        assert "Tarjeta" in routes_page.get_payment_method_text()

    def test_send_message_to_driver(self):
        routes_page = self.prepare_card_added()

        routes_page.set_driver_message(data.message_for_driver)

        assert routes_page.get_driver_message() == data.message_for_driver

    def test_order_blanket_and_tissues(self):
        routes_page = self.prepare_card_added()

        routes_page.click_manta_switch()

        assert routes_page.is_manta_switch_displayed()


    def test_order_two_ice_creams(self):
        routes_page = self.prepare_card_added()

        routes_page.click_ice_cream_plus_button(2)

        assert routes_page.get_ice_cream_counter() == "2"

    def test_driver_modal_appears(self):
        routes_page = self.prepare_order_ready()

        routes_page.click_order_taxi_final_button()

        assert "El conductor llegará" in routes_page.get_driver_modal_text()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()