# !TODO まだ移植していないのでここに書かれているコードは実行されない


class ClickEvent:
    
    #
    # 毎日クリックするだけの処理を行う（ショッピング）
    #
    def one_click_event_in_shopping(self):

        print("Main::one_click_event_in_shopping 毎日クリックするだけの処理を行う（ショッピング）")
        url = self.main_html.create_url("shopping")
        print(f"Main::one_click_event_in_shopping url: {url}")
        self.driver.get(url)
        selenium_elm = self.selenium_element(self.driver)

        # クリックする広告のフレームを取得
        btns = selenium_elm.get_elements_by_xpath('//li[@class="clickpt_ad_box"]//a[@class="go_btn "]')

        # クリック数
        count = 0

        # クリックする項目を列挙
        for btn in btns:
            # クリックする
            # 新規ページを開いちゃうから、うまくいかないかも
            btn.click()
            count += 1

        print(f"Main::one_click_event_in_shopping count: {count}")
        return
    #
    # 毎日クリックするだけの処理を行う
    #
    def one_click_event_in_daily(self):
        print("Main::one_click_event_in_daily 毎日クリックするだけの処理を行う")
        url = self.main_html.create_url("daily.php")
        print(f"Main::one_click_event_in_daily url: {url}")
        self.driver.get(url)
        selenium_elm = self.selenium_element(self.driver)

        # クリックする広告のフレームを取得
        btns = selenium_elm.get_elements_by_xpath('//div[@class="click_btn"]')
        
        # クリック数
        count = 0

        # クリックする項目を列挙
        for btn in btns:
            # クリックする
            # 新規ページを開いちゃうから、うまくいかないかも
            btn.click()
            count += 1
        
        print(f"Main::one_click_event_in_daily count: {count}")

        return
    #
    # 毎日クリックするだけの処理を行う
    #
    def one_click_event(self):
        self.one_click_event_in_shopping()
        self.one_click_event_in_daily()
        return
    