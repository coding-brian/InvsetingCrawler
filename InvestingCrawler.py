import HtmlRequest

def gethtml(starttime,endtime,url):
    data={"curr_id": 6408,
    "smlID": 1159963,
    "header": "AAPL历史数据",
    "st_date": starttime,
    "end_date": endtime,
    "interval_sec": "Daily",
    "sort_col": "date",
    "sort_ord": "DESC",
    "action": "historical_data"}

    headers={
    "content-type":"application/x-www-form-urlencoded",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "x-requested-with":"XMLHttpRequest"
    }

    response=HtmlRequest.htmlparse('post',url,data,headers)
    return response

def getresult(htmldata):
    result=[]

    table=htmldata.find(id="curr_table")
    thead=table.find('thead')

    #結果的key
    date=thead.find(attrs={'data-col-name':'date'}).text
    price=thead.find(attrs={'data-col-name':'price'}).text
    open=thead.find(attrs={'data-col-name':'open'}).text
    high=thead.find(attrs={'data-col-name':'high'}).text
    low=thead.find(attrs={'data-col-name':'low'}).text
    vol=thead.find(attrs={'data-col-name':'vol'}).text
    change=thead.find(attrs={'data-col-name':'change'}).text
    
    tr=table.find('tbody').findAll('tr')

    keylist=[date,price,open,high,low,vol,change]
    for item in tr:
        elements=item.findAll('td')
        data={}
        counter=0

        for element in elements:
            data[keylist[counter]]=element.text
            counter+=1
        result.append(data)  

    return result
