"""get hyakunin isshu"""

import sys
import urllib.request as req
from urllib import parse

def main():
    """get hyakunin isshu"""
    # コマンドライン引数を得る
    if len(sys.argv) <= 1:
        print("USAGE: hyakunin.py (keyword)")
        sys.exit()

    keyword = sys.argv[1]

    # パラメータをURLエンコードする
    api = "http://api.aoikujira.com/hyakunin/get.php"
    query = {"fmt" : "ini", "key" : keyword}
    params = parse.urlencode(query)
    url = api + "?" + params
    print("url=", url)

    # ダウンロード
    with req.urlopen(url) as requ:
        binary = requ.read()
        data = binary.decode('utf-8')
        print(data)

if __name__ == "__main__":
    main()
