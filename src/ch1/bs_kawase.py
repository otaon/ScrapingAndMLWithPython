"""test of Beautiful Soup"""

import urllib.request as req
from bs4 import BeautifulSoup

def main():
    """test of Beautiful Soup"""

    # HTMLを取得
    url = "https://api.aoikujira.com/kawase/xml/usd"
    res = req.urlopen(url)

    # HTMLを解析する
    soup = BeautifulSoup(res, 'html.parser')

    # 任意の部分を抽出する
    jpy = soup.select_one("jpy").string
    print("usd/jpy=", jpy)


if __name__ == "__main__":
    main()
