from selenium import webdriver

class seleniumDriver:
  
    #
    # 初期化
    #
    def __init__(self, driver=None):
        if driver is None:
            driver = self.__create_driver()
        self.driver = driver

    #
    # driverの作成
    #
    def __create_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome('chromedriver',options=options)
        driver.set_window_size('1200', '1000')  #大事。デフォルトが800*600になっている。headlessだと要素部分が表示されないことがあるため。
        driver.implicitly_wait(10)

        return driver

    #
    # driverを取得
    #
    def get_driver(self):
        return self.driver