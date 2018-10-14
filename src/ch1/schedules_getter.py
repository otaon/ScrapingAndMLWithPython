# """test of urllib and Beautiful Soup"""

import sys
import urllib.request as req
from bs4 import BeautifulSoup


def main():
    # """youtuber icon getter"""

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

                                    cast_infos.append({"date": date,
                                                       "hour": hour,
                                                       "minute": minute,
                                                       "caster_name": caster_name,
                                                       "cast_title": cast_title,
                                                       "img_path": img_path})

    def quote(string):
        return '"' + string + '"'

    with open("./" + save_name, mode="w") as sv:
        sv.write("date, " + "hour, " + "minute, " + "caster_name, " + "cast_title, " + "img_path" + "\n")
        for cast_info in cast_infos:
            sv.write(quote(cast_info["date"]) + ", " +
                     quote(cast_info["hour"]) + ", " +
                     quote(cast_info["minute"]) + ", " +
                     quote(cast_info["caster_name"]) + ", " +
                     quote(cast_info["cast_title"]) + ", " +
                     quote(cast_info["img_path"]))
            sv.write("\n")


if __name__ == "__main__":
    main()
