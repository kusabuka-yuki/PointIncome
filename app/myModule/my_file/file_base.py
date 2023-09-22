import os
from xml.etree.ElementTree import ElementTree

class FileBase:
    
    # xmlファイルの読み込み
    def read_xml(self, path):
        if os.path.isfile(path):
            return ElementTree().parse(path)
        else:
            print(f"{path}が存在しませんでした。")
            return False

    # textファイルの読み込み
    def read_text(self, path):
        if os.path.isfile(path):
            f = open(path, 'r', encoding='UTF-8')
            text = f.read()
            f.close
            return text
        else:
            print(f"{path}が存在しませんでした。")
            return False