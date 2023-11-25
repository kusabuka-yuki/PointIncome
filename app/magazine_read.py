from myModule.selenium_driver.selenium_element import seleniumElement
import time
import re

global logger

class MagazineRead:
    
    DISTANCE = 0
    MAX_ROOP_COUNT = 50

    #
    # 初期化
    #
    def __init__(self, path):
        # マガジンTOPページへのリンク
        self.magazine_top_path = path

    #
    # 既読の記事かどうかを返す
    #
    def is_readed(self, selenium, element):
        readed = False
        # href要素を取得
        href = element.get_dom_attribute("href")
        # スタンプの要素を取得
        stamp = selenium.get_elements_by_xpath(f'//a[@href="{href}"]//img[@class="list_stamp_img"]')

        if len(stamp) > 0:
            readed = True
        return readed
    
    #
    # コラムからリンクを取得
    #
    def get_links_from_colm(self, driver):
        # 各コラムのリンクを取得
        se = seleniumElement(driver)
        colm_links = se.get_elements_by_xpath('//li[@class="colm"]//a')
        return colm_links
    
    #
    # マガジン一覧へのパスを配列に入れる
    #
    def set_magazine_index_path(self, driver):
        # コラムからリンクを取得
        col_links = self.get_links_from_colm(driver)

        magazine_index_paths = []

        for col_link in col_links:
            magazine_index_paths.append(self.magazine_top_path + col_link.get_dom_attribute("href"))
        
        self.logger.debug(f"MagazineRead::set_magazine_index_path magazine_index_paths: {magazine_index_paths}")
        return magazine_index_paths
    
    #
    # 次へをクリックする
    #
    def get_magazine_paths_in_colm(self, driver, col_path, current_roop_count = 0):
        max_roop_count = self.MAX_ROOP_COUNT
        magazine_path = []
        path = re.sub("\?.*", "", col_path)
        roop_count = current_roop_count

        # 記事のリンクを取得する
        se = seleniumElement(driver)
        link_elms = se.get_elements_by_xpath('//ul[@class="list_wrap clearfix"]//a')

        for link_elm in link_elms:
            # 記事一覧を列挙

            self.logger.debug(f"roop_count: {roop_count}")
            if roop_count >= max_roop_count:
                # break
                return magazine_path

            # 既読の記事が出現した時点で終了
            if self.is_readed(se, link_elm):
                return magazine_path
            magazine_path.append(path + link_elm.get_dom_attribute("href"))
            roop_count = roop_count + 1

        self.logger.debug(f"===get_magazine_paths_in_colm=== magazine_path: {magazine_path} / len(magazine_path): {len(magazine_path)}")
        # if len(magazine_path) >= max_roop_count:
        #     return magazine_path
        
        # 次へボタンがあるかを確認する
        next_btn = se.get_elements_by_xpath('//a[@class="next "]')
        
        if len(next_btn) > 0:
            self.logger.debug(f"===get_magazine_paths_in_colm=== 次のページへ magazine_path: {magazine_path}")
            next_btn[0].click()
            magazine_path = magazine_path + self.get_magazine_paths_in_colm(driver, path, roop_count)
            self.logger.debug(f"===get_magazine_paths_in_colm=== 次の記事へ magazine_path: {magazine_path}")
        
        return magazine_path

    #
    # 記事一覧から全ての記事のリンクを取得
    #
    def get_magazine_path(self, driver, magazine_index_paths):

        max_roop_count = self.MAX_ROOP_COUNT

        # 記事へのリンク
        magazine_paths = []
        for path in magazine_index_paths:
            # カラム一覧を列挙
            self.logger.debug(f"MagazineRead::get_magazine_path path: {path}")
            # 記事一覧へ遷移
            driver.get(path)
            magazine_paths_count = len(magazine_paths)
            tmp_magazine_paths = self.get_magazine_paths_in_colm(driver, path, magazine_paths_count)
            magazine_paths = magazine_paths + tmp_magazine_paths

            if len(tmp_magazine_paths) >= max_roop_count:
                return magazine_paths

        self.logger.debug(f"MagazineRead::get_magazine_path magazine_paths: {magazine_paths} / magazine_paths_counts: {len(magazine_paths)}")
        return magazine_paths
    
    #
    # 次を読むをクリックする
    #
    def click_goto_next(self, driver):
        se = seleniumElement(driver)
        # 次を読むをクリックする。(スタンプをゲットするも同じ要素)
        next = se.get_elements_by_xpath('//a[@id="move_page"]')
        if len(next) > 0:
            next[0].click()
            self.click_goto_next(driver)
        return
    #
    # マガジンを読む
    #
    def read_magazine(self, driver, magazine_paths):
        stamp_get_count = 0
        roop_count = 0
        # max_roop_count = self.MAX_ROOP_COUNT
        for path in magazine_paths:
            self.logger.debug(f"MagazineRead::read_magazine path: {path}")

            # if roop_count >= max_roop_count:
            #     break

            # 記事に遷移する
            driver.get(path)
            # 次を読むをクリックする
            self.click_goto_next(driver)
            # スタンプの画面が出たら数える
            se = seleniumElement(driver)
            stamp = se.get_elements_by_xpath('//ul[@class="stamp_box"]')
            if len(stamp) > 0:
                stamp_get_count = stamp_get_count + 1
        
            # time.sleep(self.DISTANCE)
            roop_count = roop_count + 1
        
        self.logger.debug(f"スタンプを{stamp_get_count}個ゲット！！")
        return

    #
    # マガジンのリンクを取得
    #
    def read_all_magazine(self, driver):

        self.logger.debug("MagazineRead::get_magazine_links===>")

        # マガジンページにアクセス
        driver.get(self.magazine_top_path)
        
        # 各コラムのリンクを取得
        magazine_index_paths = self.set_magazine_index_path(driver)

        # 記事一覧から全ての記事のリンクを取得 -> 配列
        magazine_paths = self.get_magazine_path(driver, magazine_index_paths)

        self.logger.debug(f"count: {len(magazine_paths)}")
        # 全ての記事にアクセスしてページをめくり、スタンプゲット
        self.read_magazine(driver, magazine_paths)
        
        # 終了
        self.logger.debug("MagazineRead::get_magazine_links<===")
        return