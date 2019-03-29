from django.shortcuts import render
from datetime import datetime, timedelta
import pandas_datareader as web
from pandas_datareader._utils import RemoteDataError

def DateToString(dt):
    dt_string = '{:%Y-%m-%d}'.format(dt)                    #convert date format into string DD/MMM/YYYY
    return (dt_string)

def SimpleLastTD(lastBusDay):
    lastBusDay = lastBusDay - timedelta(days = 1)
    if datetime.weekday(lastBusDay) == 5:                   #if it's Saturday
        lastBusDay = lastBusDay - timedelta(days = 1)       #then make it Friday
    elif datetime.weekday(lastBusDay) == 6:                 #if it's Sunday
        lastBusDay = lastBusDay - timedelta(days = 2);      #then make it Friday
    return (lastBusDay)

def SimpleLastMD(today):
    first = today.replace(day=1)                            #set fist = start of month
    LastMD = SimpleLastTD(first)
    return (LastMD)

def SimpleLastYD(today):
    first = datetime(today.year, 1, 1)                      #set first = start of year
    LastYD = SimpleLastTD(first)
    return (LastYD)

class Stock():
    def __init__(self, ticker, prices):
        self.ticker = ticker
        self.prices = prices

    def Threeprices(self):
        prices3 = []
        today = datetime.now()
        prices3.append(self.prices.loc[DateToString(SimpleLastTD(today)),'Close']) # T-1 price
        prices3.append(self.prices.loc[DateToString(SimpleLastTD(SimpleLastTD(today))),'Close']) # T-2 price
        prices3.append(self.prices.loc[DateToString(SimpleLastMD(today)),'Close']) # Last month end price
        prices3.append(self.prices.loc[DateToString(SimpleLastYD(today)),'Close']) # Last year end price
        return prices3

    def stockticker(self):
        return self.ticker

    def lasttradeday(self):
        dt = datetime.now()
        return DateToString(SimpleLastTD(dt))

    def lastprice(self):
        myPrice = self.Threeprices()
        return str(round(myPrice[0], 2))

    def dailypnl(self):
        per = self.Threeprices()
        return "{:.2%}".format(per[0] / per[1] - 1)

    def mtdpnl(self):
        per = self.Threeprices()
        return "{:.2%}".format(per[0] / per[2] - 1)

    def ytdpnl(self):
        per = self.Threeprices()
        return "{:.2%}".format(per[0] / per[3] - 1)

### Main ###

dt = datetime.now()
SayToday = DateToString(dt)
start = SimpleLastYD(dt)
mydemostock = 'BABA'
mydemoprice = web.DataReader(mydemostock, 'yahoo', start, dt)           # https://finance.yahoo.com/quote/baba/history/
myForm = []
myForm.append(Stock(mydemostock, mydemoprice))

def MyView(request):
    if request.POST:
        myScrapy = request.POST['mybox']
        try:
            mytrial = web.DataReader(myScrapy, 'yahoo', start, dt)
            myForm.append(Stock(myScrapy, mytrial))
        except RemoteDataError:
            pass
    context = {'SayToday':SayToday, 'myForm':myForm}
    return render(request, 'IvanEvanglist.html', context)