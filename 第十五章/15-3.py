
from urllib import urlopen
from bs4 import BeautifulSoup

text = urlopen('https://www.python.org/jobs/').read()
soup = BeautifulSoup(text)
jobs = set()
for header in soup('h3'):
    links = header('a', 'reference')
    if not links: continue
    link = links[0]
    jobs.add('%s (%s)'%(link.string, link['herf']))

print '\n'.join(sorted(jobs, key=lambda s: s.lower))