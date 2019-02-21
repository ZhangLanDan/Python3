import requests
from fake_useragent import UserAgent
import xlwings as xw 

wb = xw.Book('zjs.xlsx')
ua = UserAgent()
headers = {'user-agent':ua.random}
sht = wb.sheets[0]
urls = sht.range('d3:d82').value
print(urls)
skus = sht.range('c3:c82').value
names = sht.range('f3:f82').value

def down(url,name):
    r = requests.get(url,headers=headers)
    with open(name,'wb') as f:
        f.write(r.content)
down(urls[0],'o.jpg')