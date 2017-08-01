
from urllib import urlopen
from HTMLParser import HTMLParser

class myScraper(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.in_h3 = False
        self.in_link = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'h3':
            self.in_h3 = True
        if tag == 'a' and 'herf' in attrs:
            self.in_link = True
            self.chunks = []
            self.url = attrs['href']

    def handle_data(self, data):
        if self.in_link:
            self.chunks.append(data)

    def handle_endtag(self, tag):
        if tag == 'h3':
            self.in_h3 = True
        if tag == 'a':
            if self.in_h3 and self.in_link:
                print '%s (%s)'%(''.join(self.chunks), self.url)
            self.in_link = False

text = urlopen('https://www.python.org/jobs').read()
parser = myScraper()
parser.feed(text)
parser.close()
