"""test of Beautiful Soup"""

import urllib.request as req
from bs4 import BeautifulSoup

def main():
    """test of Beautiful Soup"""

    # HTMLを取得
    url = "https://stocks.finance.yahoo.co.jp/stocks/detail/?code=usdjpy"
    res = req.urlopen(url)

    # HTMLを解析する
    soup = BeautifulSoup(res, 'html.parser')

    # 任意の部分を抽出する
    price = soup.select_one(".stoksPrice").string
    print("usd/jpy=", price)


if __name__ == "__main__":
    main()
