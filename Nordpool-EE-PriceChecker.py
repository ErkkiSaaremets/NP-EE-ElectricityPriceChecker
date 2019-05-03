
# https://www.nordpoolgroup.com/Market-data1/Dayahead/Area-Prices/EE/Daily/?view=table
# Thinking about building Raspberry PI electricity price monitor with Python and Flask and database.
# It should show current hourly electricity price in cents on a small external LED/LCD display.
# And warn (red font when price rises up compared to last 2-3) and 
# write the historical data to the database and draw a pretty graph which can be viewed over www.

import requests


page = requests.get('https://www.nordpoolgroup.com/api/marketdata/page/48?currency=,,EUR,EUR')

# print(page.json())
x = page.json()

#remove trash from a pile of dicts and lists to get interesting data. 
x = x.get("data")
x = x.get("Rows")
for row in range(len(x)): # remove the loop and x[0] is latest info
    # print(x[o])
    a = x[row]
    date = a["Name"]
    a = a["Columns"]
    a = a[0]
    print(date, a["Value"])
    if row == 0:
        latestprice = a["Value"]
        latestdate = date

print(f" \n latest: {latestdate}, {latestprice}")
