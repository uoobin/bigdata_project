from wordcloud import WordCloud
import matplotlib.pyplot as plt
import csv
%matplotlib inline

tot_17 = open("result_total_17.csv", "r").read().split("\n")
spr_17 = open("result_spr_17.csv", "r").read().split("\n")
smr_17 = open("result_smr_17.csv", "r").read().split("\n")
aut_17 = open("result_aut_17.csv", "r").read().split("\n")
wtr_17 = open("result_wtr_17.csv", "r").read().split("\n")

list_tot, list_spr, list_smr, list_aut, list_wtr = [], [], [], [], []
for v in tot_17:
    v = v.split(",")
    list_tot.append(v[0])
for v in spr_17:
    v = v.split(",")
    list_spr.append(v[0])
for v in smr_17:
    v = v.split(",")
    list_smr.append(v[0])
for v in aut_17:
    v = v.split(",")
    list_aut.append(v[0])
for v in wtr_17:
    v = v.split(",")
    list_wtr.append(v[0])

a = 10
season = []
spr_score, smr_score, aut_score, wtr_score = 0, 0, 0, 0
for i in range(len(list_tot)):
    if list_spr[i] in list_tot:
        spr_score += a
    if list_smr[i] in list_tot:
        smr_score += a
    if list_aut[i] in list_tot:
        aut_score += a
    if list_wtr[i] in list_tot:
        wtr_score += a
    a -= 1
        
season.append(spr_score)
season.append(smr_score)
season.append(aut_score)
season.append(wtr_score)

v = season.index(max(season))
if v == 0:
    influ = "봄"
elif v == 1:
    influ = "여름"
elif v == 2:
    influ = "가을"
else:
    influ = "겨울"

print(influ)
# my_list = []
# with open('result_total_17.csv', 'r') as f:
#     reader = csv.reader(f)
#     my_list = '\t'.join([i[0] for i in reader])
    
# wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf',max_font_size = 40, 
#                background_color = 'white').generate(my_list)

# plt.figure(figsize=(16,9))
# plt.imshow(wc, interpolation="bilinear")
# plt.axis("off")
# plt.show()