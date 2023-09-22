class HtmlBase:

    #
    # 初期化
    #
    def __init__(self, base_url="", type="", query=""):
        self.base_url = base_url
        self.create_url(type, query)
    
    #
    # URLを生成する
    #
    def create_url(self, type="", query=""):
        url = self.base_url + type
        if not query == "":
            url += "?q="
            url += query
        self.url = url

        return self.url

    #
    # URLの作成
    #
    def set_url(self, url):
        self.url = url
    
    #
    # URLの取得
    #
    def get_url(self):
        return self.url    
    #
    # BaseURLの取得
    #
    def get_base_url(self):
        return self.base_url
