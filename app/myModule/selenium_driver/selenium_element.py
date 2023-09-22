from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium_driver.driver import seleniumDriver

class seleniumElement(seleniumDriver):
    #
    # 初期化
    #
    def __init__(self, driver=None):
        # myDriverクラスの初期化
        super().__init__(driver)

        # Webドライバーの取得
        self.driver = super().get_driver()
        # print(f"seleniumElement::__init__ self.driver -> {self.driver}")

    #
    # XPATHからエレメントを取得
    #
    def get_elements_by_xpath(self, path):
        # print(f"seleniumElement::get_elements_by_xpath self.driver -> {self.driver}")
        self.driver.save_screenshot("obj/debug/1.png")

        return self.driver.find_elements(By.XPATH, path)

    #
    # XPATHからエレメントを取得
    #
    def get_element_by_xpath(self, path, index = 0):
        elements = self.get_elements_by_xpath(path)
        # print(f"seleniumElement::get_element_by_xpath elements -> {elements}")
        if len(elements) > 0:
            return elements[index]
        else:
            return None

    #
    # 指定箇所までスクロールする
    #
    def scroll_page(self, path):
        # 末尾から2番目の要素がいいらしい　https://self-development.info/selenium%E3%81%A7twitter%E3%82%92%E3%82%B9%E3%82%AF%E3%83%AC%E3%82%A4%E3%83%94%E3%83%B3%E3%82%B0%E3%81%99%E3%82%8B%E3%80%90python%E3%80%91/
        target = self.get_element_by_xpath(path, -2)
        # スクロール
        actions = ActionChains(self.driver)
        actions.move_to_element(target)
        actions.perform()