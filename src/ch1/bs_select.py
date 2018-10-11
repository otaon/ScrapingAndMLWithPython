"""test of urllib and Beautiful Soup"""

from bs4 import BeautifulSoup

def main():
    """test of urllib and Beautiful Soup"""

    path = "tolstoy.html"

    # urlopen()でデータを取得
    with open(path) as f:
        # ファイル全体を文字列として取得する
        tolstoy = f.read()

        # BeautifulSoupで解析
        soup = BeautifulSoup(tolstoy, "html.parser")

        # 必要な部分をCSSクエリで取り出す
        ## タイトル部分を取得
        print("h1 =", soup.select_one("div#meigen > h1").string)
        ## リスト部分を取得
        for li in soup.select("div#meigen > ul.items > li"):
            print("li =", li.string)


if __name__ == "__main__":
    main()
