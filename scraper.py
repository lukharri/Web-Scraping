import urllib.request 
import re

urls = ["http://google.com", "http://nytimes.com", "http://cnn.com"]

i = 0
regex = '<title>(.+?)</title>'
pattern = re.compile(regex)

while i < len(urls):
    with urllib.request.urlopen(urls[i]) as response:
        htmltext = response.read()
    titles = re.findall(pattern, htmltext)
    print (titles)
    i+=1
