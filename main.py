import HtmlRequest

url='https://cn.investing.com/instruments/HistoricalDataAjax'


data={"curr_id": 6408,
"smlID": 1159963,
"header": "AAPL历史数据",
"st_date": "2021/08/30",
"end_date": "2021/09/06",
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

result=response.find(id="curr_table")


# table=response.find(class_="instrumentHeader")


print(result)
