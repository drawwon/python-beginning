
import urllib
from subprocess import Popen, PIPE
text = urllib.urlopen('www.taobao.com').read()
tidy = Popen('tidy',stdin=PIPE, stdout=PIPE, stderr=PIPE)
tidy.stdin.write(text)
tidy.stdin.close()
print tidy.stdout.read()