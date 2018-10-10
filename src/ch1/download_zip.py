"""download zip code"""

import urllib.request
import urllib.parse


def main():
    """download zip code"""

    api = "http://api.aoikujira.com/zip/xml/get.php"

    # パラメータをURLエンコードする
    values = {'fmt' : 'xml', 'zn' : '1500042'}
    params = urllib.parse.urlencode(values)

    # リクエスト用のURLを生成
    url = api + "?" + params
    print("url=", url)

    # ダウンロード
    data = urllib.request.urlopen(url).read()
    text = data.decode("utf-8")
    print(text)


if __name__ == "__main__":
    main()
