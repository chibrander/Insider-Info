import pandas as pd

def ceobuy(ticker):
    hf = pd.read_html("http://openinsider.com/screener?fd=0&fdr=&td=0&tdr=&s=" + ticker + "&o=&t=p&minprice=&maxprice=&v=0&isceo=1&iscfo=1&sicMin=&sicMax=&sortcol=0&maxresults=500")

    return hf[5]

#print(ceobuy("INTL"))


def trade(tradetype):
    hf = pd.read_html("http://openinsider.com/screener?fd=0&fdr=&td=0&tdr=&s=&o=&t=" + tradetype + "&minprice=1&maxprice=&v=0&isceo=1&iscfo=1&sicMin=&sicMax=&sortcol=0&maxresults=1000&excludeDerivRelated=1")

    return hf[5]

#print(trade("s"))
trade("s").to_excel("sales.xlsx")
trade("p").to_excel("purchases.xlsx")


def trade(tradetype):
    hf = pd.read_html("http://openinsider.com/screener?fd=0&fdr=&td=0&tdr=&s=&o=&t=" + tradetype + "&minprice=1&maxprice=&v=0&isceo=1&iscfo=1&sicMin=&sicMax=&sortcol=0&maxresults=1000&excludeDerivRelated=1")

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
    df['Filing Day'] = df['Filing Date'].apply(convertdate)
    #df['Shares Traded'] = df['Shares Traded'].apply(convertnumber)
    df['Value Traded'] = df['Value Traded'].apply(convertnumber)
    #df['Shares Owned'] = df['Shares Owned'].apply(convertnumber)
    return df

df1 = tradedetails("p",25000,"","",0,1,1,0,0,0,"")
df2 = tradedetails("s",25000,"","",0,1,1,0,0,0,"")

cleandataframe(df1)
cleandataframe(df2)
readydata = pd.concat([df1,df2])
readydata.to_excel("readydata.xlsx")
