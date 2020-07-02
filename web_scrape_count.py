from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_695859.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
total = 0
count = 0
tags = soup('span')

for tag in tags:
    num = int(tag.contents[0])
    count = count + 1
    total = total + num

'''for tag in tags:
    tag_split = tag.decode().split('>')
    tag_split2 = tag_split[1].split('<')
    tag_num = int(tag_split2[0])
    total = total + tag_num
    count = count + 1'''

print('Count', count)
print('Sum', total)
    
    