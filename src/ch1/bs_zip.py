"""test of urllib and Beautiful Soup"""

import urllib.request as req
import sys
from bs4 import BeautifulSoup

def main():
    """test of urllib and Beautiful Soup"""

    # 引数のバリデーション
    if len(sys.argv) != 2:
        print("USAGE: python bs_zip.py zip-code")
        sys.exit()

    # 引数の形式のバリデーション
    zip_code = sys.argv[1]
    if len(zip_code) != 7:
        print("USAGE: zip-code must be 7 length of numbers")
        sys.exit()

    # 引数の数値のバリデーション
    try:
        int(zip_code)
    except ValueError:
        print("USAGE: zip-code 7 length of numbers")
        sys.exit()

    url = "http://api.aoikujira.com/zip/xml/" + zip_code

    # urlopen()でデータを取得
    with req.urlopen(url) as res:
        # BeautifulSoupで解析
        soup = BeautifulSoup(res, "html.parser")
        ken = soup.find("ken").string
        shi = soup.find("shi").string
        cho = soup.find("cho").string
        print(ken, shi, cho)


if __name__ == "__main__":
    main()
