"""test of Beautiful Soup"""

from bs4 import BeautifulSoup

def main():
    """test of Beautiful Soup"""

    # 解析したいHTML
    html = """
    <html>
        <body>
            <ul>
                <il><a href="http://uta.pw">uta</a></li>
                <il><a href="http://oto.chu.jp">oto</a></li>
            </ul>
        </body>
    </html>
    """

    # HTMLを解析する
    soup = BeautifulSoup(html, 'html.parser')

    # find_all()メソッドで取り出す
    links = soup.find_all("a")

    print("links", links)
    print("type", type(links))

    # リンク一覧を表示
    for a in links:
        href = a.attrs['href']
        text = a.string
        print(text, ">", href)


if __name__ == "__main__":
    main()
