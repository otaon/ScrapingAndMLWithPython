# """test of urllib and Beautiful Soup"""

import sys
import urllib.request as req
from bs4 import BeautifulSoup
import datetime as dt
import re


def main():
    # """youtuber icon getter"""

    # iconと所属対応一覧
    icon_dict = {"upd8.png": "upd8",
                 "appland.png": ".LIVE",
                 "cover.png": "cover",
                 "amaryllis.png": "アマリリス組",
                 "paryi.png": "パリィ",
                 "zig.png": "zig",
                 "nijisanji.png": "にじさんじ",
                 "nijisanji_seeds.png": "にじさんじSEEDs",
                 "animare.png": "あにまーれ",
                 "hnst.png": "HoneyStrap",
                 "vlive.png": "ぶいらいぶ",
                 "reality-": "REALITY",
                 "/openrec-": "OPENREC.tv",
                 "ichinana-": "イチナナ",
                 "shovel.png": "ShoveL",
                 "iwamotocho.png": "岩本町芸能社"}

    # 引数のバリデーション
    if len(sys.argv) <= 1:
        print("USAGE: python schedules_getter.py URL save_name")
        sys.exit()
    elif len(sys.argv) == 2:
        print("default URL: https://virtual-youtuber.userlocal.jp/schedules")
        url = "https://virtual-youtuber.userlocal.jp/schedules"
        save_name = sys.argv[1]
    elif len(sys.argv) == 3:
        url = sys.argv[1]
        save_name = sys.argv[2]
    else:
        print("USAGE: python schedules_getter.py URL save_name")
        sys.exit()

    # 公開されている全配信情報
    cast_infos = []

    with req.urlopen(url) as res:
        soup = BeautifulSoup(res, "html.parser")
        schedules = soup.select_one(".table")

        for schedule_tr1 in schedules.find_all("tr"):
            # 改行のみの要素は無視
            if schedule_tr1.text == "\n":
                continue

            # 日付を取得
            if schedule_tr1.attrs:
                date = schedule_tr1.find("td").text.strip()
                # "月"がついていたら保持する
                if re.match(r"[0-9]+月", date):
                    month = re.sub(r"([0-9]+月).*", r"\1", date)
                continue

            for schedule_td in schedule_tr1.find_all("td"):
                # 改行のみの要素は無視
                if schedule_td.text == "\n":
                    continue

                # 時間を取得
                if "text-right" in schedule_td.attrs["class"]:
                    hour = schedule_td.text.strip()
                    continue

                schedule_td_divs = schedule_td.find_all("div")
                for schedule_td_div in schedule_td_divs:
                    # 改行のみの要素は無視
                    if schedule_td_div.text == "\n":
                        continue

                    if "d-flex" in schedule_td_div.attrs["class"] \
                            and "justify-content-start" in schedule_td_div.attrs["class"] \
                            and "flex-ie" in schedule_td_div.attrs["class"] \
                            and "mt-1" in schedule_td_div.attrs["class"]:
                        for schedule_td_div_div in schedule_td_div.find_all("div"):
                            # 改行のみの要素は無視
                            if schedule_td_div_div.text == "\n":
                                continue

                            # 分を取得
                            if "text-right" in schedule_td_div_div.attrs["class"]:
                                minute = schedule_td_div_div.text.strip()
                                continue

                            if "vertical" in schedule_td_div_div.attrs["class"] \
                                    and "flex-fill" in schedule_td_div_div.attrs["class"] \
                                    and "pl-2" in schedule_td_div_div.attrs["class"]:
                                for schedule_td_div_div_span in schedule_td_div_div.find_all("span", recursive=False):
                                    # 改行のみの要素は無視
                                    if schedule_td_div_div_span.text == "\n":
                                        continue

                                    # 配信情報を取得
                                    img_path = schedule_td_div_div_span.find("img").attrs["src"]
                                    cast_title = schedule_td_div_div_span.find("a").text
                                    caster_name = schedule_td_div_div_span.find("span").find("a").text

                                    # dateを月日合わせて、配信時間を"yyyy/m/dTh:m"の書式にする
                                    if not re.match(r"[0-9]+月", date):
                                        date = month + date

                                    # 日時配信情報を登録
                                    cast_infos.append({"date": date,
                                                       "hour": hour,
                                                       "minute": minute,
                                                       "caster_name": caster_name,
                                                       "cast_title": cast_title,
                                                       "img_path": img_path})

    def convert_timestamp(_date, _hour, _minute):
        # """タイムスタンプを文字列からISO8601形式に変換する ex '2010-04-01T16:00:00+00:00'
        year = dt.date.today().year
        month = int(re.sub(r"([0-9]+)月.*", r"\1", _date))
        date = int(re.sub(r"[0-9]+月([0-9]+)日.*", r"\1", _date))
        hour = int("{:1}".format(int(_hour.rstrip("時"))))
        minute = int("{:1}".format(int(_minute.rstrip("分"))))

        return dt.datetime(year, month, date, hour, minute).strftime('%Y-%m-%dT%H:%M') + ":00+00:00"

    def quote(string):
        # """文字列をクォートする
        return '"' + string + '"'

    with open("./" + save_name, mode="w") as sv:
        sv.write("datetime, " + "caster_name, " + "cast_title, " + "belonging" + "\n")
        for cast_info in cast_infos:
            # 所属を判別する
            belonging = "Other"
            for icon in icon_dict.keys():
                if icon in cast_info["img_path"]:
                    belonging = icon_dict[icon]
                    break

            sv.write(quote(convert_timestamp(cast_info["date"], cast_info["hour"], cast_info["minute"])) +
                     ", " +
                     quote(cast_info["caster_name"]) + ", " +
                     quote(cast_info["cast_title"]) + ", " +
                     quote(belonging))
            sv.write("\n")


if __name__ == "__main__":
    main()
