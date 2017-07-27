import urllib
import re


html_file = urllib.urlopen("http://money.cnn.com/quote/quote.html?symb=AAPL")
html_text = html_file.read()
#regex = '<td class="wsod_last" nowrap="nowrap">(.+?)</td>'
regex = '<span stream="last_211573" streamformat="ToHundredth" streamfeed="SunGard">(.+?)</span>'
pattern = re.compile(regex)
price = re.findall(pattern, html_text)
print price
    
