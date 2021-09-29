import InvestingCrawler
import json

starttime=input('請輸入查詢開始日期(格式:2021/09/01)')
endtime=input('請輸入查詢結束日期(格式:2021/09/20)')

url='https://cn.investing.com/instruments/HistoricalDataAjax'

htmldata=InvestingCrawler.gethtml(starttime,endtime,url)

result=InvestingCrawler.getresult(htmldata)

jsonresult=json.dumps(result, ensure_ascii=False, indent = 4).encode('utf8').decode()

print(jsonresult)
