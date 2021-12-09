import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.bnr.ro/files/xml/nbrfxrates2021.htm")
table = browser.find_element(By.XPATH, '//*[@id="Data_table"]')
header = browser.find_element(By.XPATH, '//*[@id="Data_table"]/table/thead/tr').text.split("\n")
table_text = table.text
lista = table_text.split('\n')
# print(lista)
dictionar = {i: [] for i in header}

for j in range(0, len(header)):
    for i in range(len(header) + int(j), len(lista), len(header)):
        dictionar[header[int(j)]].append(lista[i])
print(dictionar)
df = pd.DataFrame(dictionar)
df.to_csv("BNR_ALL_DATA.csv")
time.sleep(5)
browser.close()