import urllib.request

# 保存対象URL
url = "http://uta.pw/shodou/img/28/214.png"
# URLと保存パスを指定
savename = "test.png"

# ダウンロードしてファイルを保存する
urllib.request.urlretrieve(url, savename)
print("保存しました")

