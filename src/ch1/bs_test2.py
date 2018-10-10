"""test of Beautiful Soup"""

from bs4 import BeautifulSoup

def main():
    """test of Beautiful Soup"""

    # 解析したいHTML
    html = """
    <html>
    <body>
    <h1 id="title">スクレイピングとは？</h1>
    <p id="body">Webページから任意のデータを抽出すること。</p>
    </body>
    </html>
    """

    # HTMLを解析する
    soup = BeautifulSoup(html, 'html.parser')

    # 任意の部分を抽出する
    id_title = "title"
    id_body = "body"
    title = soup.find(id=id_title)
    print(id_title + " = " + title.string)
    body = soup.find(id=id_body)
    print(id_body + " = " + body.string)

if __name__ == "__main__":
    main()
