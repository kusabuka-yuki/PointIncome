class seleniumBrowser:
  
    #
    # 初期化
    #
    def __init__(self, driver=None):
        print("Browser::__init__")
        self.__driver = driver

    #
    # 新しいwindowを開く
    #
    def open_window(self):
        print("Browser::open_window")
        self.__driver.execute_script("window.open('');")
    
    #
    # windowを閉じる
    #
    def close_window(self, tab_num = -1):
        print("Browser::close_window")
        self.switch_tab(tab_num)
        print(self.__driver.window_handles)
        self.__driver.close()
        print(self.__driver.window_handles)
        self.switch_tab(tab_num)

    #
    # タブの切り替え
    #
    def switch_tab(self, tab_num):
        print("Browser::switch_tab")
        self.__driver.switch_to.window(self.__driver.window_handles[tab_num])

