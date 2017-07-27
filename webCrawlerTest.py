

# web crawler that finds all URLs connected to a given URL

import urlparse
import urllib
from bs4 import BeautifulSoup
import re

# URL seed - visit TechAnnounce homepage
url = "http://www.techannounce.ttu.edu/Client/default.aspx"

# list of URLs to visit
urls = [url]

# record of visited URLs
visited = [url]  


# traverse initial URL and find all hyperlinks of the form
# http://www.techannounce.ttu.edu/Client/ViewMessage.aspx?MsgId=(.+?)
while len(urls) > 0:
    try:
 #       regex = "http://www.techannounce.ttu.edu/Client/ViewMessage.aspx?MsgId=(.+?)"
#        pattern = re.compile(regex)
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
    for link in soup.find_all('a'):
        print link
 #       tag['href'] = urlparse.urljoin(url, tag['href'])

        # add new URLs and update visited list
#        if url in tag['href'] and tag['href'] not in visited:
#            urls.append(tag['href'])
#            visited.append(tag['href'])

print visited
        
        
        
                                  
