import unittest
import time
from utilities.utilities import WebDriverElements
from functions.loginValidations.loginValidations import LoginValidations


class LoginValidationsTests(unittest.TestCase):
    def setUp(self):
        self.driver_paths = WebDriverElements()
        self.driver = self.driver_paths.get_driver()
        self.driver.get("https://modeloparaganar.com.mx/")

    # Valida que el campo Username sea obligatorio
    def test_01_validate_user_name(self):
        loginValidations = LoginValidations(self.driver)
        loginValidations.login('', '12345')
        time.sleep(2)

        # Assert para validar la alerta
        expected_text = "x\nPor favor, ingresa tus datos y una contraseña para completar el registro"
        alert_text = loginValidations.user_name_required()
        self.assertEqual(alert_text, expected_text, f"NO se está validando que el campo Username sea requerido. "
                                                    f"Se esperaba: '{expected_text}', pero se obtuvo: '{alert_text}'.")

    # Valida que el campo Password sea obligatorio
    def test_02_validate_user_pass(self):
        loginValidations = LoginValidations(self.driver)
        loginValidations.login('12222222', '')
        time.sleep(2)

        # Assert para validar la alerta
        expected_text = "x\nNúmero del Cliente o contraseña incorrecta"
        alert_text = loginValidations.user_password_required()
        self.assertEqual(alert_text, expected_text, f"NO se está validando que el campo Password sea requerido. "
                                                    f"Se esperaba: '{expected_text}', pero se obtuvo: '{alert_text}'.")

    # Finaliza el test
    def tearDown(self):
        time.sleep(1)
        print('¡Se ha completado el Test Aumatico!')
        loginValidations = LoginValidations(self.driver)
        loginValidations.close()

    if __name__ == '__main__':
        unittest.main()
