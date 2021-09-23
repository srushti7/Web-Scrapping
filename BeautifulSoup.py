# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 19:03:32 2021

@author: Srushti
"""

from bs4 import BeautifulSoup


html_doc = """<html>

<body>
<h1>My First Heading</h1>
<b>!-------This is a comment line-------!</b>
<p title = "About Me" class = "test"> My first paragraph</p>

<div class = "Cities">
<h2>Paris</h2>
</div>
</body>
</html>"""


soup = BeautifulSoup(html_doc, 'html.parser')



print(type(soup))

print (soup)

tag = soup.p
print(tag)

comment = soup.b.string
print(type(comment))

print(comment)
print(tag.attrs)



