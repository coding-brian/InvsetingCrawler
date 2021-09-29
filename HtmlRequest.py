import requests
from bs4 import BeautifulSoup

def htmlparse(method,url,data,headers):
    if method=='get':
        #網站的request請求
        r=requests.get(url,headers=headers)
        r.encoding='utf-8'
        #html分析
        html_doc=r.text
        soup=BeautifulSoup(html_doc,'html.parser')

        return soup
    elif method=='post' : 
        response=requests.post(url,headers=headers,data=data)

        response.encoding='utf-8'
        #html分析
        html_doc=response.text
        soup=BeautifulSoup(html_doc,'html.parser')
        return soup