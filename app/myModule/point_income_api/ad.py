#
# 広告クラス
#
from point_income_api import base
from selenium_driver.selenium_element import seleniumElement

class Ad(base.Base):
    def __init__(self):
        return
    
    # 広告を閉じる
    def close(self, driver):
        selenium_element = seleniumElement(driver)
        close_btns = selenium_element.get_elements_by_xpath('//button[@id="cboxClose"]')

        if len(close_btns) > 0:
            # とりあえず、最前となる広告を一つと考えて消す
            close_btn = close_btns[0]
            close_btn.click()
        return