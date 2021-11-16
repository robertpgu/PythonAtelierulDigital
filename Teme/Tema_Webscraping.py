import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get("https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/")
link = BeautifulSoup(r.text, "html.parser")
title = link.find_all('div')
header = []
data_list = []
ok = 0

for i in title:
    for tr_index in i.find_all('table'):
        if ok == 0:
            td_list = []
            for j, td_index in enumerate(list(tr_index.find_all('tr'))):
                if j == 0:
                    header = [td_index.get_text().split('\n')[1], td_index.get_text().split('\n')[2], td_index.get_text().split('\n')[4]]
                else:
                    td_list = td_index.get_text().split('\n')
                if len(td_list) > 0:
                    list1 = [td_list[1], td_list[2], td_list[4]]
                else:
                    continue
                data_list.append(list1)
                ok = 1
        else:
            break


for date in range(20, 27):
    strr = "https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-"+str(date)+"-ianuarie-ora-13-00/"
    header.append(str(date)+" ianuarie")
    r = requests.get(strr)
    link = BeautifulSoup(r.text, "html.parser")
    title = link.find_all('div')
    ok = 0
    for t in title:
        for tr_index in t.find_all('table'):
            if ok == 0:
                td_list = []
                for j, td_index in enumerate(list(tr_index.find_all('tr'))):
                    if j == 0:
                        continue
                    else:
                        td_list = td_index.get_text().split('\n')
                    if len(td_list) > 4:
                        data_list[j-1].append(td_list[4])
                    else:
                        data_list[j-1].append('-')
                    # data_list.append(list1)
                    ok = 1
            else:
                break
    r.close()

data_list = data_list[0:-2]
print(data_list)
print(header)
df = pd.DataFrame(data_list, columns=header)
df.to_csv('Gov-Covid.csv', header=header)

