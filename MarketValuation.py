import re
import lxml.html
import requests

# GDP from st louis fed
GDP = requests.get('http://research.stlouisfed.org/fred2/data/GDP.txt')
print '---------------'
GDP_date_values_raw = re.findall('\d+\-\d+\-\d+\s+\d+\.\d*', GDP.content)
GDP_date_values = []

for item in GDP_date_values_raw:
    GDP_date_values.append(item.split())
    # .append or .extend

for i in GDP_date_values:
    print i

# get wilshire 5000 prices from yahoo
html = lxml.html.parse('http://finance.yahoo.com/q/hp?s=^W5000+Historical+Prices')

#print(html)
#print lxml.html.tostring(html)

# return values from within all tr and td elements using xpath
# save those values in 'r' list
r = html.xpath('//tr/td/text()')

print '---------------'

# keep track of list's index location
count = 0
for i in r:
    # use regex to find entries with date values
    if re.findall('\w+\s\d+,\s\d+', i):
        # print date
        print i
       # print close price
        print r[count + 4]
    count += 1


