'''
Avoid looking for spoilers.

Forums: Python Challenge Forums, read before you post.
IRC: irc.freenode.net #pythonchallenge

Version : Python 3.7.4

정규식 참조
ref : https://ko.wikipedia.org/wiki/%EC%A0%95%EA%B7%9C_%ED%91%9C%ED%98%84%EC%8B%9D

'''

from bs4 import BeautifulSoup as BS, Comment
import requests
import re

url = "http://www.pythonchallenge.com/pc/def/equality.html"
resp = requests.get(url)
html = resp.text

soup = BS(html, 'html.parser')

for comments in soup.findAll(text=lambda text:isinstance(text, Comment)):
    comments.extract()

temp = re.findall(r'[^A-Z]+[A-Z]{3}([a-z]{1})[A-Z]{3}[^A-Z]+',comments)

result=""
for i in temp:
    result=result+i

print(result)



