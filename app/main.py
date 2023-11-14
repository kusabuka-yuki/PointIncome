import sys
import time
import configparser

class Main:

    config = configparser.ConfigParser()
    config.read('../conf/config.ini', encoding='utf-8')

    HOME_DIR_PATH = config['DEFAULT']['HomeDir']
    ORIGIN_URL = "https://pointi.jp/"
    CONFIG_PATH = ""
    MY_MODULE_PATH = config['DEFAULT']['ModulePath']
    CONFIG_PATH = HOME_DIR_PATH + "conf/"
    TARGET_USER = ""
    USER_WORK_FILE_PATH = ""
    DIFFUSION_TWEET_PATH = ""

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
        read_appconfig = read_config.ReadConfig(appconfig_path)
        webconfig_path = self.CONFIG_PATH + "webconfig.xml"
        read_webconfig = read_config.ReadConfig(webconfig_path)
        
        read_webconfig.set_config()
        self.webconfig = read_webconfig.get_config()
        read_appconfig.set_config()
        self.appconfig = read_appconfig.get_config()
        self.email_address = self.appconfig["ADDRESS"] 
        self.password = self.appconfig["PASSWORD"]

        print(f"init::HOME_DIR {self.HOME_DIR_PATH}")
        print(f"init::MY_MODULE_PATH {self.MY_MODULE_PATH}")
        print(f"init::self.email_address {self.email_address}")
        print(f"init::self.password {self.password}")

    #
    # 毎日クリックするだけの処理を行う（ショッピング）
    #
    def one_click_event_in_shopping(self):
        try:
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
        except Exception as e:
            print(e)
        return
    #
    # 毎日クリックするだけの処理を行う
    #
    def one_click_event_in_daily(self):
        try:
            print("Main::one_click_event_in_daily 毎日クリックするだけの処理を行う")
            url = self.main_html.create_url("daily.php")
            print(f"Main::one_click_event_in_daily url: {url}")
            self.driver.get(url)
            selenium_elm = self.selenium_element(self.driver)

            # クリックする広告のフレームを取得
            btns = selenium_elm.get_elements_by_xpath('//div[@class="go_btn"]')
            
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
        except Exception as e:
            print(e)
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
        email_address = self.email_address
        password = self.password
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
        try:
            self.driver = self.selenium_driver().get_driver()

            self.login()

            # クリックするだけの処理を行う
            self.one_click_event()

            # マガジンを読んでスタンプを貯める
            magazine = self.magazine_read(self.webconfig["MAGAZINE"])
            magazine.read_all_magazine(self.driver)
        except Exception as e:
            print(e)
        return

if __name__ == "__main__":
    time_start = time.time()
    print("start program")
    start = Main()
    start.main()
    print("finish program")
    time_end = time.time()
    print(f"===> {time_end - time_start}")
    sys.exit()