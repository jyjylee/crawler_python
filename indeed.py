import requests as rq
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&as_src=&radius=25&l=%EA%B2%BD%EA%B8%B0%EB%8F%84+%EA%B3%A0%EC%96%91&fromage=any&sort=&psf=advsrch&from=advancedsearch&limit={LIMIT}"

def extract_indeed_pages():
    indeed_result = rq.get(URL)
    indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")
    pagination = indeed_soup.find("div",{"class":"pagination"})

    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))
        #print("page name: ", pages)

    max_page = pages[-1]

    return max_page


def extract_indeed_jobs(last_page):
    for page in range(last_page):
        result=rq.get(f"{URL}&start = {page*LIMIT}")
        print(result.status_code)

