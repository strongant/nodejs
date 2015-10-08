# _*_coding: UTF-8_*_
__author__ = 'bwh'

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint


class MyHTMLParser(HTMLParser):
    "得到开始标签"
    def handle_starttag(self, tag, attrs):
        print('<%s>'%tag)
    def handle_endtag(self, tag):
        print('</%s>'%tag)
    def handle_startendtag(self, tag, attrs):
        print('<%s/>'%tag)
    def handle_data(self, data):
        print(data)
    def handle_comment(self, data):
        print(data)
    def handle_entityref(self, name):
        print('&%s;'%name)
    def handle_charref(self, name):
        print('&#%s;'%name)


parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')


