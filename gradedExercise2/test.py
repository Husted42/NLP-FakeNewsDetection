##### -- Imports -- #####
import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

#### -- Variables -- #####
newsFront = 'https://www.bbc.com/news'
data = '''<div class="gs-c-promo-body gel-1/2@xs gel-1/1@m gs-u-mt@m"><div><a class="gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor" href="/news/world-us-canada-64740209"><h3 class="gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text">US TV reporter and child killed in Florida attack</h3></a><p class="gs-c-promo-summary gel-long-primer gs-u-mt nw-c-promo-summary">Dylan Lyons is named as the journalist killed while reporting the fatal shooting of a woman in Orlando.</p></div><ul class="gs-o-list-inline gs-o-list-inline--divided gel-brevier gs-u-mt-"><li class="nw-c-promo-meta"><span class="gs-c-timestamp gs-o-bullet gs-o-bullet- nw-c-timestamp"><span class="gs-o-bullet__icon gel-icon"><svg viewbox="0 0 32 32"><polygon points="17,15.4 17,6 15,6 15,16.6 23.8,21.7 24.8,19.9"></polygon><path d="M16,4c6.6,0,12,5.4,12,12c0,6.6-5.4,12-12,12S4,22.6,4,16C4,9.4,9.4,4,16,4 M16,0C7.2,0,0,7.2,0,16c0,8.8,7.2,16,16,16 s16-7.2,16-16C32,7.2,24.8,0,16,0L16,0z"></path></svg></span><time class="gs-o-bullet__text date qa-status-date gs-u-align-middle gs-u-display-inline" data-datetime="4h" data-seconds="1677163623" datetime="2023-02-23T14:47:03.000Z"><span aria-hidden="true" class="qa-status-date-output">4h</span><span class="gs-u-vh">4 hours ago</span></time></span></li><li class="nw-c-promo-meta"><a aria-label="From US &amp; Canada" class="gs-c-section-link gs-c-section-link--truncate nw-c-section-link nw-o-link nw-o-link--no-visited-state" href="/news/world/us_and_canada"><span aria-hidden="true">US &amp; Canada</span></a></li></ul></div>'''

def getData(data):
    response = requests.get(data)
    contents = response.text
    return contents

def getSummary(m):
    m = re.search(r'<p(?:.*?)>.*<\/p>', m)
    m = m.group(0)
    return m

def Div(data):
    soup = BeautifulSoup(getData(data), 'html.parser')
    soupList = soup.find_all('div', class_='gs-c-promo-body gel-1/2@xs gel-1/1@m gs-u-mt@m') 
    lst = []
    for i in range (0, 4):
        print(getSummary(str(soupList[i])))

print(getSummary(data))
print(Div(newsFront))

def cleanAll(input):
    tag = ['p', 'span', 'a', 'i']
    text = input
    text = re.sub(r'(<strong(?:.*?)>).*(<\/strong>)', '', text)
    text = re.sub(r'\s+', ' ', text)
    for element in tag:
        x = '<' + element + '(?:.*?)>'
        y = '<\/' + element + '>'
        text = re.sub(x, '', text)
        text = re.sub(y, ' ', text) 
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\s,', '', text)
    text = re.sub('\<br(.*)', '', text)
    text = re.sub('\<img(.*)', '', text)
    text = re.sub('\<b(.*)', '', text)
    return text

def getHeader(input):
    text = input.find('span', class_='mw-page-title-main')
    text = str(text)
    cleanAll(text)
    return text

def getDate(input):
    text = input.find('strong', class_='published')
    text = str(text)
    text = re.sub(r'<strong(?:.*?)>', '', text)
    text = re.sub(r'<\/strong>', ' ', text)
    text = re.sub(r'<span(?:.*?)>', '', text)
    text = re.sub(r'<\/span>', ' ', text)
    return text

def getContent(input):
    text = input.find_all('p')
    lst = []
    for elm in text:
        elm = str(elm)
        lst.append(elm)

    string = ' '.join(lst)
    string = cleanAll(string)
    return string

def articleList():
    def temp(input):
        page = 'https://en.wikinews.org/w/index.php?title=Category:Politics_and_conflicts&from=' + input
        divGroup = BeautifulSoup(getData(page), 'html.parser')
        divGroup = divGroup.find_all('div', id='mw-pages')
        divGroup = divGroup[0].find_all('div', class_='mw-category-group')
        divGroup = divGroup[0].find_all('a')
        lst = []
        for element in divGroup: 
            element = str(element)
            href_regex = r'href="([^"]+)"'
            element = re.search(href_regex, element)
            element = element.group(1)
            element = 'https://en.wikinews.org/' + element
            lst.append(element)
        return lst
    letters = "ABCDEFGHIJKLMNOPRSTUVWZABCDEFGHIJKLMNOPRSTUVWZ"[10%23:10%23+10]
    letters = [*letters]
    lst = []
    for elemement in letters:
        elemement = temp(elemement)
        lst = lst + elemement
    return lst

def createTable():
    links = (articleList())[:10]
    lst = []
    for elm in links: 
        response = requests.get(elm)
        contents = response.text
        x = BeautifulSoup(contents, 'html.parser')
        x = [getHeader(x), getDate(x), getContent(x)]
        lst.append(x)

    df = pd.DataFrame(lst)
    df.columns = ['header', 'summary', 'content']
    return df
print(createTable())