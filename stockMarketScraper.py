import urllib
import re

# list of markets to scrape data about
markets = ["Dow Jones", "S&P 500", "NASDAQ", "Global DOW"]

# url identifier for ea market
stock_markets = ["djia", "spx", "comp", "gdow"]


# visit each URL and retrieve current market value
i = 0
while i < len(stock_markets):
    
    url = "http://www.marketwatch.com/investing/index/" + stock_markets[i]

    # open url and read html text
    html_text = urllib.urlopen(url).read()

    # construct regex to find data
    regex = '<p class="data bgLast">(.+?)</p>'
    
    # compile a regular expression pattern into a regular exression object
    pattern = re.compile(regex)

    # find all instances in html text that match regex
    avg = re.findall(pattern, html_text)

    # display current stock market average
    print "The ", markets[i], "is currently at ", avg[0]
    i+=1



resources = ["Gold", "Oil"]
resource_markets = ["gold", "crude%20oil%20-%20electronic"]

i = 0
while i < len(resource_markets):
    
    url = "http://www.marketwatch.com/investing/future/" + resource_markets[i]

    # open url and read html text
    html_text = urllib.urlopen(url).read()

    # construct regex to find data
    regex = '<p class="data bgLast">(.+?)</p>'
    
    # compile a regular expression pattern into a regular exression object
    pattern = re.compile(regex)

    # find all instances in html text that match regex
    avg = re.findall(pattern, html_text)

    # display current stock market average
    print "The ", resources[i], "market is currently at ", avg[0]
    i+=1
