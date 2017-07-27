import urllib
import re

# URLs to visit
urls = ["http://youtube.com", "http://google.com", "http://nytimes.com", "http://cnn.com",
        "http://yahoo.com", "http://netflix.com", "http://facebook.com", "http://twitter.com",
        "http://amazon.com", "http://wikipedia.com"]

# use regex (.+?) to retrieve website titles
regex = '<title>(.+?)</title>'

# compile a regular expression pattern into a regular exression object
pattern = re.compile(regex)

i = 0
while i < len(urls):

    # open a url and read the html text
    request = urllib.urlopen(urls[i])
    htmltext = request.read()

    # find and display the website title
    titles = re.findall(pattern, htmltext)
    print titles
    i+=1
