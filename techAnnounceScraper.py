import BeautifulSoup
import urllib
import re

url = "http://www.techannounce.ttu.edu/Client/default.aspx"
url_msg = "http://www.techannounce.ttu.edu/Client/ViewMessage.aspx?MsgId="

announcement_urls = [url]

# retrieve all announcement urls from techAnnounce homepage
try:
    html = urllib.urlopen(url).read()
except:
    print url

soup = BeautifulSoup(html, "html.parser")

for tag in soup.find_all('a', href=True):
    tag['href'] = urlparse.urljoin(url, tag['href'])
    if url_msg in tag['href'] and tag['href'] not in announcement_urls:
        #print tag['href'] 
        announcement_urls.append(tag['href'])


# open ea announcement url and retrieve the title, content, and categorie(s)
while len(announcement_urls) > 0:
    try:
        html = urllib.urlopen(announcement_urls[0]).read()
    except:
        print announcement_urls[0]
        
    announcement_urls.pop(0)

    soup2 = BeautifulSoup(html, "html.parser")


# search html for date announcements were posted
date_regex = '<span id="lbl_CurDate">(.+?)</span>'
date_pattern = re.compile(date_regex)
date = re.findall(date_pattern, html)
print date[0]



