from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class BaseUITest:

    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--disable-browser-side-navigation")

        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.implicitly_wait(5)
        self.is_driver_remote = False
        self.session_id = self.driver.session_id

    def teardown(self):
        self.driver.quit()
