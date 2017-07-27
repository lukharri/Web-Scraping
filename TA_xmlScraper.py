# Luke Harris - tech announce scraper

from bs4 import BeautifulSoup
import urllib
import re


# scrape the date of most recent announcement post
def get_post_date():
    # specify url to be accessed
    url = "http://www.techannounce.ttu.edu/Client/default.aspx"

    # request html from Tech Announce homepage
    try:
        html = urllib.urlopen(url).read()
    except:
        print url

    # use regular expression to parse html for date info
    date_regex = '<span id="lbl_CurDate">(.+?)</span>'
    date_pattern = re.compile(date_regex)
    date = re.findall(date_pattern, html)
    print str(date[0])
    print ''



# scrape most recently posted announcements
def get_announcements():
    # retrieve XML from tech announce
    url2 = "http://www.techannounce.ttu.edu/Client/ViewRss.aspx"
    xml = urllib.urlopen(url2).read()
    soup = BeautifulSoup(xml, "lxml")


    # For each announcement find and display the following items
    # 1. title
    # 2. body
    # 3. categorie(s)

    # Mark announcements that offer something for free such as workshops, seminars,
    # concerts, food, etc...
    for item in soup.find_all('item'):
        for child in item.children:
            if "title" in str(child):
                print child.string.upper()
            if "description" in str(child):
                print child.string
            if "free" in str(child) or "Free" in str(child) or "FREE" in str(child):
                print "Free: TRUE"
            if "category" in str(child):
                print child.string
        print ''
        print ''



def main():
    get_post_date()
    get_announcements()


main()






