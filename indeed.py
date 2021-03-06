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


def extract_job(html):
    ##Title
    title = html.find("h2",{"class":"title"}).find("a")["title"]

    ##Company-Name
    company_name=""
    company = html.find("div",{"class":"sjcl"}).find("div").find("span",{"class":"company"})
    company_anchor =company.find("a")
    
    ##Location
    location_span = html.find("div",{"class":"sjcl"}).find("span",{"class":"location accessible-contrast-color-location"})
    location_div = html.find("div",{"class":"sjcl"}).find("div",{"class":"location accessible-contrast-color-location"})

    if location_span is not None:
        location=str(location_span.string)
    else:
        location=str(location_div.string)
    
    if company_anchor is not None:
        company_name=str(company_anchor.string.strip())
    else:
        company_name=str(company.string.strip())
    return {'title':title, 'company': company_name, 'location': location}

def extract_indeed_jobs(last_page):
    jobs=[]
    last_page=1
    for page in range(last_page):
        result=rq.get(f"{URL}&start = {page*LIMIT}")
        soup =BeautifulSoup(result.text,"html.parser")
        results=soup.find_all("div",{"class": "jobsearch-SerpJobCard"})
        for result in results:
            job=extract_job(result)
            jobs.append(job)
    return jobs
