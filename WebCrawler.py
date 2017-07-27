# web crawler that finds all URLs connected to a given URL
import re
import urlparse
import urllib
from bs4 import BeautifulSoup

# URL seed - visit TechAnnounce homepage
# url = "http://www.techannounce.ttu.edu/Client/default.aspx"
url = "http://winwebcrawler.com"

# list of URLs to visit
urls = [url]

# record of visited URLs
visited = [url]  


# traverse initial URL and find all hyperlinks of the form
# http://www.techannounce.ttu.edu/Client/ViewMessage.aspx?MsgId=(.+?)
while len(urls) > 0:
    try:
        htmltext = urllib.urlopen(urls[0]).read()
    except:
        print urls[0]
        
    # create Beautiful Soup object
    soup = BeautifulSoup(htmltext, "html.parser")

    # remove each url from the list after it is visited
    urls.pop(0)

    # display how many new URLs are added each iteration
    print len(urls)

    # find all hypertext references and add hostname 
    for tag in soup.findAll('a', href = True):
        tag['href'] = urlparse.urljoin(url, tag['href'])

        # add new URLs and update visited list
        if url in tag['href'] and tag['href'] not in visited:
            urls.append(tag['href'])
            visited.append(tag['href'])

print visited
        
        
        
                                  
