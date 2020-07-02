'''The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract 
the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:'''
import urllib
from urllib.request import urlopen
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#prompt for url   #http://py4e-data.dr-chuck.net/comments_42.json
site = input('Enter location: ')

print('Retrieving http:', site)

#read json data from url using urlib
uh = urllib.request.urlopen(site, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')

info = json.loads(data)

#parse and extract comment counts
count = 0
total = 0
for item in info['comments']:
    count += 1
    total += int(item['count'])

#compute the sum
print('Count:', count)
print('Sum:', total)








