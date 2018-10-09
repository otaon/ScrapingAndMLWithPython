"""IPアドレス確認APIを使用して情報を取得する"""
import urllib.request

if __name__ == "__main__":
    def main():
        """main"""
        # get data information
        url = "http://api.aoikujira.com/ip/ini"
        res = urllib.request.urlopen(url)
        data = res.read()

        # convert binary data to utf-8 string data
        text = data.decode("utf-8")
        print(text)

main()
