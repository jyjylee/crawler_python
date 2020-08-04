import os
import math
import requests as rq
from bs4 import BeautifulSoup

indeed_result=rq.get("https://kr.indeed.com/jobs?q=python&l=%EA%B2%BD%EA%B8%B0%EB%8F%84+%EA%B3%A0%EC%96%91")
indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")
 
pagination= indeed_soup.find("div",{"class":"pagination"})

pages= pagination.find_all('a')
spans=[]
for page in pages:
    spans.appen(page.find("span"))
spans=spans[:-1]
