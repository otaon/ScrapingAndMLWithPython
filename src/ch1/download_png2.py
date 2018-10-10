"""save downloaded file"""
import urllib.request

def main():
    """main"""
    # URLと保存パスを指定
    url = "http://uta.pw/shodou/img/28/214.png"
    savename = "test.png"

    # ダウンロードしてメモリに保持
    mem = urllib.request.urlopen(url).read()

    # ファイルに保存
    with open(savename, mode="wb") as fil:
        fil.write(mem)
        print("保存しました")

if __name__ == "__main__":
    main()
