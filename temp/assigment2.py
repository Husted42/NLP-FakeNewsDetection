import re
import requests
from bs4 import BeautifulSoup
import re 

response = requests.get('https://www.bbc.com/news')
contents = response.text

def getData(data):
    response = requests.get(data)
    contents = response.text
    return contents

def matches(data):
    regexHeder = re.compile(r'<h\d(?:.*?)>(.*?)<\/h\d>')
    matches = regexHeder.findall(getData(data))
    return matches


def headerList(matchLst):
    lst = []
    for elements in matchLst:
        elements = elements.replace("&#x27;", '')
        elements = re.sub(r'<span(?:.*?)>', '', elements)
        elements = re.sub(r'<\/span>', ' ', elements)
        lst.append(elements)
    return lst

print("")
print("requestList")
print(headerList(matches(newsFront)))

print("")
print("soupList")
soup = BeautifulSoup(getData(newsFront), 'html.parser')
regexHeder = re.compile(r'<h\d(?:.*?)>(.*?)<\/h\d>')
suppe = soup.find_all('h2') + soup.find_all('h3')

lst2 = []
for elements in suppe:
    elements = str(elements)
    elements = re.sub(r'<h\d(?:.*?)>', '', elements)
    elements = re.sub(r'<\/h\d>', '', elements)
    elements = re.sub(r'<span(?:.*?)>', '', elements)
    elements = re.sub(r'<\/span>', ' ', elements)
    lst2.append(elements)

print(lst2)
print(len(lst2))
