"""test of Beautiful Soup"""

from bs4 import BeautifulSoup

def main():
    """test of Beautiful Soup"""

    # 解析したいHTML
    html = """
    <html>
    <body>
    <h1>スクレイピングとは？</h1>
    <p>Webページを解析すること。</p>
    <p>任意の箇所を抽出すること。</p>
    </body>
    </html>
    """

    # HTMLを解析する
    soup = BeautifulSoup(html, 'html.parser')

    # 任意の部分を抽出する
    h1 = soup.html.body.h1
    print("h1 = " + h1.string)
    p1 = soup.html.body.p
    print("p = " + p1.string)
    p2 = p1.next_sibling.next_sibling
    print("p = " + p2.string)

if __name__ == "__main__":
    main()
