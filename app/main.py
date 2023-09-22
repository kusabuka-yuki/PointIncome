import sys
import click_event

class Main:

    HOME_DIR_PATH = "/home/ec2-user/solutions/PointIncame/"
    ORIGIN_URL = "https://pointi.jp/"
    CONFIG_PATH = ""
    MY_MODULE_PATH = HOME_DIR_PATH + "app/myModule"
    CONFIG_PATH = HOME_DIR_PATH + "conf/"
    TARGET_USER = ""
    USER_WORK_FILE_PATH = ""
    DIFFUSION_TWEET_PATH = ""
    EMAIL_ADDRESS = "kchobimmcl@yahoo.co.jp"
    PASSWORD = "07120908"

    def __init__(self):
        print(self.MY_MODULE_PATH)
        sys.path.append(self.MY_MODULE_PATH)

        from my_file.file_base import FileBase
        from my_html.html_base import HtmlBase
        from selenium_driver.driver import seleniumDriver
        from selenium_driver.selenium_element import seleniumElement
        from point_income_api.login import Login
        from point_income_api.ad import Ad
        import magazine_read
        import read_config
        
        self.file_base = FileBase
        self.html_base = HtmlBase
        self.main_html = self.html_base(self.ORIGIN_URL)
        self.selenium_driver = seleniumDriver
        self.selenium_element = seleniumElement
        self.point_income_api_login = Login
        self.point_income_api_ad = Ad
        self.magazine_read = magazine_read.MagazineRead
        self.read_config = read_config.ReadConfig

        # 設定ファイルを読み込む
        appconfig_path = self.CONFIG_PATH + "appconfig.xml"
        appconfig = read_config.ReadConfig(appconfig_path)
        webconfig_path = self.CONFIG_PATH + "webconfig.xml"
        read_webconfig = read_config.ReadConfig(webconfig_path)
        
        read_webconfig.set_config()
        self.webconfig = read_webconfig.get_config()

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

        self.driver.save_screenshot("obj/debug/shopping.png")
        
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
        
        self.driver.save_screenshot("obj/debug/daily.png")
        print(f"Main::one_click_event_in_daily count: {count}")

        return
    #
    # 毎日クリックするだけの処理を行う
    #
    def one_click_event(self):
        self.one_click_event_in_shopping()
        self.one_click_event_in_daily()
        return
    
    # 動画を見る処理
    # def watch_cm_event(self):
    #     self.cm_html = self.html_base("https://pointi.cmnw.jp/")
    #     url = self.cm_html.create_url("cm")
    #     return

    #
    # ログイン
    #
    def login(self):

        # サイトを表示した際に表示される無駄な広告を閉じる
        ad = self.point_income_api_ad()
        login = self.point_income_api_login()
        ad.close(self.driver)

        # ログイン 
        email_address = self.EMAIL_ADDRESS
        password = self.PASSWORD
        result = login.login(self.driver, email_address, password)

        if result == False:
            # 正常にログインできなかった場合はプログラムを終了する
            print("progam has bat status.")
            return
        
        print("logined")
        
        # サイトを表示した際に表示される無駄な広告を閉じる
        ad.close(self.driver)

        return

    def main(self):
        self.driver = self.selenium_driver().get_driver()

        self.login()

        # クリックするだけの処理を行う
        self.one_click_event()

        # マガジンを読んでスタンプを貯める
        magazine = self.magazine_read(self.webconfig["MAGAZINE"])
        magazine.read_all_magazine(self.driver)

        return

if __name__ == "__main__":
    print("start program")
    start = Main()
    start.main()