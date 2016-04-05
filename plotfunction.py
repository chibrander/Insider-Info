    # import pandas as pd
    #
    # https://www.quandl.com/api/v3/datasets/WIKI/GOOGL.csv?start_date=2014-01-01&end_date=2016-01-14&order=asc&api_key=dbGk5UrFde_r6bzkHLj5&column_index=11
import pandas as pd
import Quandl
import matplotlib.pyplot as plt

def draw(tick):
    #import numpy as np

    mydata = Quandl.get("WIKI/" + tick)


    #markers_on = np.array(['2013-02-26','2015-01-26','2016-02-26', '2016-04-01'], dtype='datetime64')
    #df3 = pd.DataFrame(markers_on)
    #df4 = df3.set_index(0)
    #df5 = df4.join(mydata,how='left')
    #df6 = df5['Adj. Close']
    #mynewdata = mydata.join(df6,how="left",lsuffix='_OG',rsuffix='_Mark')


    #get trading start

    def tradedetails(tradetype,tradevalue,minprice,maxprice,isofficer,ceo,cfo,isdir,is10,isother,stock):
        hf = pd.read_html("http://openinsider.com/screener?fd=0&fdr=&td=0&tdr=&s="+ stock + "&o=&t="+ tradetype + "&minprice=" + str(minprice) + "&maxprice=" + str(maxprice) + "&v="+ str(tradevalue) +"&isofficer=" + str(isofficer) + "&isceo=" + str(ceo) + "&iscfo=" + str(cfo) + "&isdirector=" + str(isdir) + "&istenpercent=" + str(is10) + "&isother=" + str(isother) + "&sicMin=&sicMax=&sortcol=1&maxresults=1000")
        return hf[5]

    def convertdate(x):
        return x[5:7] + "/" + x[8:10] + "/" + x[0:4]

    def converttime(x):
        return x[11:]

    def convertnumber(x):
        return x.replace("+","").replace("$","").replace(",","")

    def cleandataframe(df):
        df['Trade Date'] = df['Trade Date'].apply(convertdate)
        df['Filing Time'] = df['Filing Date'].apply(converttime)
        df['Filing Date'] = df['Filing Date'].apply(convertdate)
        #df['Shares Traded'] = df['Shares Traded'].apply(convertnumber)
        df['Value Traded'] = df['Value Traded'].apply(convertnumber)
        #df['Shares Owned'] = df['Shares Owned'].apply(convertnumber)
        return df

    def cleanerdataframe(df):
        df['Trade Date'] = df['Trade Date'].apply(convertdate)
        df['Filing Time'] = df['Filing Date'].apply(converttime)
        df['Filing Date'] = df['Filing Date'].apply(convertdate)
        df['Shares Traded'] = df['Shares Traded'].apply(convertnumber)
        df['Value Traded'] = df['Value Traded'].apply(convertnumber)
        #df['Shares Owned'] = df['Shares Owned'].apply(convertnumber)
        return df


    detail = tradedetails("p",25000,"","",0,1,1,0,0,0,tick)
    pd.to_datetime(detail['Trade Date'])
    detail = detail.set_index('Trade Date')
    newdetail = detail.join(mydata,how='left')
    df6 = newdetail['Adj. Close']
    mynewdata = mydata.join(df6,how="left",lsuffix='_OG',rsuffix='_Mark')

    #get trading end

    plt.plot(mynewdata['Adj. Close_OG'])
    plt.plot(mynewdata['Adj. Close_Mark'],marker='o',color='r', markersize=11)
    plt.show()

rawstocks = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies",header=0)
stockstable = rawstocks[0]
stocks = stockstable['Ticker symbol']
stockslist = stocks.tolist()

for stock in stockslist[0:11]:
    try:
        draw(stock)
    except:
        pass
