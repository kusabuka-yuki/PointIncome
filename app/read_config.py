import glob
from enum import Enum
from myModule.my_file.file_base import FileBase

class ReadConfig:
    # 初期化処理
    def __init__(self, path):
        self.path = path
        self.config = ""
    
    # configファイルの読み込み
    def __load_config(self, path):

        xml = FileBase().read_xml(path)

        config = {}

        if xml:
            # XMLファイルを読み込めた場合
            # 一番上はBODY要素
            for parent in xml:
                for children in parent:
                    config[children.tag] = children.text
            return config
        else:
            return -1

    # configファイルの取得
    def set_config(self, path=""):

        if len(path) > 0:
            # pathがあればpathを入れる
            target_path = path
        else:
            # pathがなければself.pathを入れる
            target_path = self.path
        
        try:
            # target_path = target_path + "*.xml"
            print(f"ReadConfig::set_config target_path -> {target_path}")
            glob_files = glob.glob(target_path)
        except:
            print("set_config have exception on ReadConfig")

        config = ""
        if len(glob_files) > 0:
            xml_path = glob_files[0]
            config =  self.__load_config(xml_path)
        else:
            print("configファイルがありません。")

        self.config = config
    
    # configファイルの取得
    def get_config(self):
        return self.config