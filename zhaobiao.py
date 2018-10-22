#coding=utf-8
import requests
import lxml
from bs4 import BeautifulSoup
target_url = "http://www.qianlima.com/zb/area_305/"
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
header = {"User-Agent":user_agent}
html = requests.get(target_url,headers=header)
content = html.text
soup = BeautifulSoup(content,'lxml')
tag = soup.find_all("div",class_="shixian_zhaobiao")
for tag_div in tag:
    tag_a = tag_div.find_all('a')
    for a in tag_a:
        print (a["href"])
        print (a.string)
        print (a.next_element.next_element.string)
        print (a.parent.next_sibling)
for tag_dl in tag:
    tag_dl = tag_dl.find("dl")
    print (tag_dl.get_text())

