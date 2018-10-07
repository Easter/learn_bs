#coding=utf-8
html_doc = """
<html><head><title>The Dormouse's story</title></head>
    <body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc,"lxml")
for child in soup.title.children:
    print child
#print soup.body.contents[2].contents
head_tag = soup.head
title_tag = head_tag.contents[0]
print title_tag
print title_tag.contents
body_tag = soup.body
print body_tag.contents[0]
print body_tag.contents[1]
print body_tag.contents[2]
print body_tag.contents[3].contents
for child in body_tag.contents[3].contents:
    print child
print ".............>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
for child in body_tag.children:
    print child
print ".............>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
for child in body_tag.contents:
    print child
print body_tag.contents
print body_tag.children
#.children无法以列表形式显示出来（具体返回什么格式以后再考察）。只能用来进行循环。但是.contents可以，用途更广泛
for child in head_tag.descendants:
    print child
print head_tag.descendants#以未知格式输出，运行查看
print len(soup.contents)
print len(list(soup.descendants))
#.strings方法返回类型
print soup.strings
for string in soup.strings:
    print string
#得到的结果中有许多空格，可以用stripped_strings去掉
for string in soup.stripped_strings:
    print string
link = soup.a
print link.parents
for parent in link.parents:
    if parent is None:
        print parent
    else:
        print parent.name
print len(list(link.parents))
print list(link.parents)
sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></a>","lxml")
print sibling_soup.prettify()
for sibling in soup.a.next_siblings:
    print repr(sibling)