import HtmlRequest

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}

response=HtmlRequest.htmlparse('get',f"https://cn.investing.com/equities/apple-computer-inc-historical-data",data="",headers=headers)

table=response.find(id="curr_table")

print(table)
