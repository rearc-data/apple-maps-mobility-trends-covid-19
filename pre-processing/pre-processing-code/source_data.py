
import os
import boto3
from urllib.request import urlopen
from html.parser import HTMLParser
import pandas as pd

class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.data = None
        self.match = False

    def handle_starttag(self, tag, attr):
        if tag.lower() == 'div':
            for item in attr:
                if item[0].lower() == 'class' and item[1] == 'download-button-container':
                    if self.match == False:
                        self.match = True
                        break
        if tag.lower() == 'a' and self.match == True:
            for item in attr:
                if item[0].lower() == 'href' and item[1].endswith('.csv'):
                    if self.data == None:
                        self.data = item[1]
                        break

    def handle_endtag(self, tag):
        if tag.lower() == 'div' and self.match == True:
            self.match = False


def source_dataset(s3_bucket, new_s3_key):
    source = 'https://www.apple.com/covid19/mobility'

    html = urlopen(source)
    str_html = html.read().decode()

    parser = MyHTMLParser()
    parser.feed(str_html)

    print(parser.data)


source_dataset(1, 2)