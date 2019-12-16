import requests
from bs4 import BeautifulSoup
import pandas as pd
import konlpy
from konlpy.tag import Okt
from collections import Counter
import csv
import re

f = open("prj_total_18.csv", "w", encoding="utf-8", newline='')
wr = csv.writer(f)
wr.writerow(["date", "word", "count"])

dt_index = pd.date_range(start='20180101', end='20181231')
dt_list = dt_index.strftime("%Y%m%d").tolist()

stopword = open("korean_stop_words.csv", "r").read()
stopword = stopword.replace(",", "").split('\n')

for date in dt_list:
    page = 1
    while (page != 0):
        raw = requests.get("https://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&oid=032&listType=title&date="+str(date)+"&page="+str(page),
                           headers={"User-Agent":"Mozilla/5.0"})
        html = BeautifulSoup(raw.text, 'html.parser')

        page_list = list(html.select("div.paging a"))
        cnt_page = len(page_list) + 1

        titles = html.select("div.list_body li")

        for t in titles:
            try:
                title = t.select_one("dt.photo a").text
                title = t.select_one("dt:nth-of-type(2) a").text
            except:
                title = t.select_one("a").text

            title = title.replace(",", " ")
            title = title.replace("文", "문재인")
            title = title.replace("靑", "청와대")
            title = title.replace("韓", "대한민국")
            title = title.replace("北", "북한")
            title = title.replace("中", "중국")
            title = title.replace("美", "미국")
            title = title.replace("日", "일본")
            title = title.replace("英", "영국")
            title = title.replace("與", "여당")
            title = title.replace("野", "야당")
            title = title.replace("檢", "검찰")
            title = title.replace("法", "법원")

            title = re.sub('\[[^)]+\]', '', title)
            title = re.sub('\([^)]+\)', '', title)

            tagger = Okt()
            mal_tot = tagger.pos(title, norm=True, stem = True)

            data_tot = []
            for word in mal_tot:
                if word[1] in ['Noun'] and len(word[0]) > 1:
                    if word[0] not in stopword:
                        data_tot.append(word[0])

            for value in data_tot:
                wr.writerow([date, value, 1])
        
        page += 1
        if page > cnt_page:
            page = 0
                    
f.close()

data = open("prj_total_18.csv", "r", encoding="utf-8").read()
line = list(data.split('\n'))

spr = open("prj_18_spr.csv", "w", encoding="utf-8", newline='')
spr_wr = csv.writer(spr)
spr_wr.writerow(["word", "count"])
dt_spr = pd.date_range(start='20180301', end='20180531')
spr_list = dt_spr.strftime("%Y%m%d").tolist()

smr = open("prj_18_smr.csv", "w", encoding="utf-8", newline='')
smr_wr = csv.writer(smr)
smr_wr.writerow(["word", "count"])
dt_smr = pd.date_range(start='20180601', end='20180831')
smr_list = dt_smr.strftime("%Y%m%d").tolist()  

aut = open("prj_18_aut.csv", "w", encoding="utf-8", newline='')
aut_wr = csv.writer(aut)
aut_wr.writerow(["word", "count"])
dt_aut = pd.date_range(start='20180901', end='20181130')
aut_list = dt_aut.strftime("%Y%m%d").tolist()    

wtr = open("prj_18_wtr.csv", "w", encoding="utf-8", newline='')
wtr_wr = csv.writer(wtr)
wtr_wr.writerow(["word", "count"])
dt_wtr1 = pd.date_range(start='20180101', end='20180228')
dt_wtr2 = pd.date_range(start='20181201', end='20181231')
wtr_list1 = dt_wtr1.strftime("%Y%m%d").tolist()
wtr_list2 = dt_wtr2.strftime("%Y%m%d").tolist()
wtr_list = wtr_list1 + wtr_list2

for l in line:
    l = l.split(",")
    if l[0] in spr_list:
        spr_wr.writerow([l[1], l[2]])
    if l[0] in smr_list:
        smr_wr.writerow([l[1], l[2]])
    if l[0] in aut_list:
        aut_wr.writerow([l[1], l[2]])
    if l[0] in wtr_list:
        wtr_wr.writerow([l[1], l[2]])  

spr.close()    
smr.close()    
aut.close()   
wtr.close()