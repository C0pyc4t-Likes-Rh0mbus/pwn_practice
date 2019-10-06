'''
Avoid looking for spoilers.

Forums: Python Challenge Forums, read before you post.
IRC: irc.freenode.net #pythonchallenge

Version : Python 3.7.4

'''

from bs4 import BeautifulSoup as BS, Comment
import requests

url = "http://www.pythonchallenge.com/pc/def/ocr.html"
resp = requests.get(url)
html = resp.text

soup = BS(html, 'html.parser')

for comments in soup.findAll(text=lambda text:isinstance(text, Comment)):
    comments.extract()

comment_list = list(comments)

result=""
n=0
for i in comment_list:
    if comment_list[n] < "a":
        pass
    elif comment_list[n] > "z":
        pass
    else:
        result = result+comment_list[n]
    n=n+1

print(result)