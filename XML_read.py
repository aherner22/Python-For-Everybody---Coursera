'''In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. 
The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the 
comment counts from the XML data, compute the sum of the numbers in the file.'''

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

site = input('Enter location: ')

print('Retrieving http:', site)
uh = urllib.request.urlopen(site, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

total = 0
count = 0
for item in tree.findall('.//count'):
    num = (int(item.text))
    total += num
    count += 1

print('Count:', count)
print('Sum:', total)
    