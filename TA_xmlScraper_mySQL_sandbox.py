# Luke Harris - tech announce scraper with mySQL functionality

import mysql.connector
from bs4 import BeautifulSoup
import urllib
import re


# establish connection with database
config = {
    'user' : 'root',
    'password' : '',
    'host' : 'localhost',
    'database' : 'TechAnnounce',
    'raise_on_warnings' : True,
    }

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()



# open Tech Announce homepage
url = "http://www.techannounce.ttu.edu/Client/default.aspx"
try:
    html = urllib.urlopen(url).read()
except:
    print "Failed to open: ", url 
    

# search html for date announcements were posted
date_regex = '<span id="lbl_CurDate">(.+?)</span>'
date_pattern = re.compile(date_regex)
date = re.findall(date_pattern, html)
date_str = date[0]


# retrieve XML from tech announce
xml_url = "http://www.techannounce.ttu.edu/Client/ViewRss.aspx"
xml = urllib.urlopen(xml_url).read()
xml_soup = BeautifulSoup(xml, "lxml")


# For each announcement find and display the following information
# 1. title
# 2. body
# 3. categorie(s)
# Mark announcements that offer something for free such as workshops, seminars,
# concerts, food, etc...
empty = ''
for item in xml_soup.find_all('item'):
    cat_list = []
    for child in item.children:
        if "title" in str(child):
            title = child.string.upper()
        if "description" in str(child):
            body = child.string
        if "category" in str(child):
            cat_list.append(child.string)
    if 'free' in title or 'Free' in title or 'FREE' in title or 'free' in body or 'Free' in body or 'FREE' in body:
        free = '1'
    else:
        free = '0'
    

    # determine num of categories in an announcement and insert scraped info into db
    # for announcements with 3 categories
    if len(cat_list) == 3:
        cat1 = cat_list[0]
        cat2 = cat_list[1]
        cat3 = cat_list[2]
        try:
            announcement = (date_str, str(title), str(body), str(cat1), str(cat2), str(cat3), free)
            add_announcement = ("INSERT INTO Announcements "
                            "(date, title, body, cat1, cat2, cat3, free) "
                            "VALUES (%s, %s, %s, %s, %s, %s, %s)")
            cursor.execute(add_announcement, announcement)
        except UnicodeEncodeError as ude:
            print "Insertion failed due to UnicodeEncodeError: ", title

    # for announcements with 2 categories       
    elif len(cat_list) == 2:
        cat1 = cat_list[0]
        cat2 = cat_list[1]
        try:
            announcement = (date_str, str(title), str(body), str(cat1), str(cat2), empty, free)
            add_announcement = ("INSERT INTO Announcements "
                            "(date, title, body, cat1, cat2, cat3, free) "
                            "VALUES (%s, %s, %s, %s, %s, %s, %s)")
            cursor.execute(add_announcement, announcement)
        except UnicodeEncodeError as ude:
            print "Insertion failed due to UnicodeEncodeError: ", title

    # for announcements with 1 category       
    else:
        cat1 = cat_list[0]
        try:
            announcement = (date_str, str(title), str(body), str(cat1), empty, empty, free)
            add_announcement = ("INSERT INTO Announcements "
                            "(date, title, body, cat1, cat2, cat3, free) "
                            "VALUES (%s, %s, %s, %s, %s, %s, %s)")
            cursor.execute(add_announcement, announcement)
        except UnicodeEncodeError as ude:
            print "Insertion failed due to UnicodeEncodeError: ", title
        
    # Ensure data is committed to the database
    cnx.commit()

# close database connection   
cursor.close()
cnx.close()







