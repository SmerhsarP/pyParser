import requests
from bs4 import BeautifulSoup as bs

headers = { 'accept': '*/*',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36' }
base_url = 'https://perm.hh.ru/search/vacancy?area=72&clusters=true&enable_snippets=true&search_period=30&text=python&page=1'

def hh_parse(base_url, headers):
    jobs = []
    session = requests.Session()
    request = session.get(base_url, headers = headers)
    if request.status_code == 200:
        print('OK')
        soup = bs(request.content, 'html.parser')
        divs = soup.find_all('div', attrs={'data-qa': 'vacancy-serp__vacancy'})
        for div in divs:
            title = div.find('a', attrs={'data-qa':'vacancy-serp__vacancy-title'}).text
            href = div.find('a', attrs={'data-qa':'vacancy-serp__vacancy-title'})['href']
            company = div.find('a', attrs={'data-qa':'vacancy-serp__vacancy-employer'}).text
            text1 = div.find('div', attrs={'data-qa':'vacancy-serp__vacancy_snippet_responsibility'}).text
            text2 = div.find('div', attrs={'data-qa':'vacancy-serp__vacancy_snippet_requirement'}).text
            content = text1 + ' ' + text2
            jobs.append({
                'title': title,
                'href': href,
                'company': company,
                'content': content
            })
            # print(jobs)
        print(len(jobs))

    else:
        print('ERROR')

hh_parse(base_url, headers)
