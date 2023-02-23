import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.bbc.com/news')
contents = response.text

#Match headers
regexHeder = re.compile(r'<h\d(?:.*?)>(.*?)<\/h\d>')
matches = regex.findall(contents)
print(matches)
print(len(matches))