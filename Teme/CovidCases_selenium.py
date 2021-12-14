import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/")
table = browser.find_element(By.TAG_NAME, 'tbody')
rows = table.find_elements(By.TAG_NAME, 'tr')
lista = []
for item in rows:
    lista.append(list(map(lambda x: x.text, item.find_elements(By.TAG_NAME, 'td'))))

df = pd.DataFrame(lista)
df.to_csv("Covid_data.csv")
time.sleep(5)
browser.close()