import os
import math
import requests as rq
from bs4 import BeautifulSoup

indeed_result=rq.get("https://kr.indeed.com/jobs?q=python&l=%EA%B2%BD%EA%B8%B0%EB%8F%84+%EA%B3%A0%EC%96%91")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")
 
pagination= indeed_soup.find("div",{"class":"pagination"})

links= pagination.find_all('a')
pages=[]
for link in links[:-1]:
    pages.append(int(link.string))
    print("page name: ", pages)

max_page = pages[-1]
print(pages[-1])