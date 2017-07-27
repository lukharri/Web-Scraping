# Luke Harris - test connection to mySQLdb

#from __future__ import print_function
import mysql.connector


# supply login credentials and choose which database to access
config = {
    'user' : 'root',
    'password' : '',
    'host' : 'localhost',
    'database' : 'TechAnnounce',
    'raise_on_warnings' : True,
    }


# open a connection to db
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()


# ANNOUNCEMENT #1
# Create some announcement data 
post_date = '4/20/2016'
title = "The CS department at TTU rocks!"
body = 'Are you interested in computer science? Come take a tour of the CS department.'
cat1 = 'Departmental'
cat2 = 'Academic'
cat3 = 'Prospective Students'
free = 0


# save announcement to the db 
# cursor.execute("INSERT INTO table VALUES (%s, %s, %s)", (var1, var2, var3))
#cursor.execute("INSERT INTO Announcements VALUES (%s, %s, %s, %s, %s, %s, %s)", (post_date, title, body, cat1, cat2, cat3, free))
announcement = (post_date, title, body, cat1, cat2, cat3, free)
#cursor.execute("INSERT INTO Announcements VALUES (?,?,?,?,?,?,?)", (date, title, body, cat1, cat2, cat3, free))
add_announcement = ("INSERT INTO Announcements "
                    "(date, title, body, cat1, cat2, cat3, free) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s)")
cursor.execute(add_announcement, announcement)


# ANNOUNCEMENT #2
# how about another announcement just for fun
post_date = '4/20/2016'
title = "ACM meeting tonight! Come hang out and eat some free food!"
body = 'The ACM will meet today in HH120 at 6:30pm. A surprise speaker will be there! Free food!'
cat1 = 'Student Organizations'
cat2 = 'Campus Life'
cat3 = ''
free = 1


# cursor.execute("INSERT INTO table VALUES (%s, %s, %s)", (var1, var2, var3))
cursor.execute("INSERT INTO Announcements VALUES (%s, %s, %s, %s, %s, %s, %s)", (post_date, title, body, cat1, cat2, cat3, free))
cnx.commit()


# close connection 
cursor.close()
cnx.close()


print 'Announcements successfully saved on: ', post_date













'''
# date, title, body, cat1, cat2, cat3, free
#add_announcement = """INSERT INTO Announcements VALUES (%s, %s, %s, %s, %s, %s, %s), (today, ann_title, ann_body, ann_cat1, ann_cat2, ann_cat3, boolean)"""

#cursor.execute(add_announcement)
'''
