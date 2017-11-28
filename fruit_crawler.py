import json
import datetime

import requests

tpe = datetime.timezone(datetime.timedelta(hours=8))

#today_dt = datetime.date.today()
today_dt = datetime.datetime(year=2017, month=11, day=27)
today_dt = datetime.datetime(today_dt.year, today_dt.month, today_dt.day).replace(tzinfo=tpe)

def gen_stransdate(dt):
    dt_str = dt.strftime('%Y/%m/%d').split('/')
    stransdate = "%s/%s/%s" % (dt.year - 1911, dt_str[1], dt_str[2])
    return stransdate

url = "http://amis.afa.gov.tw/fruit/FruitProdDayTransInfo.aspx"
data = json.loads(r'''{
    "ctl00$ScriptManager_Master": "ctl00$ScriptManager_Master|ctl00$contentPlaceHolder$btnQuery",
    "__EVENTTARGET": "",
    "__EVENTARGUMENT": "",
    "__VIEWSTATE": "/wEPDwUJMjYxMTk5NzY4D2QWAmYPZBYCAgMPZBYCAgsPZBYOAgEPDxYCHgRUZXh0BRXnlKLlk4Hml6XkuqTmmJPooYzmg4VkZAIHDw8WAh8ABQkxMDYvMTEvMjhkZAIJDw9kFgIeBXN0eWxlBQ1kaXNwbGF5Om5vbmU7ZAILDw8WAh8ABQkxMDYvMTEvMjgWAh8BBQ1kaXNwbGF5Om5vbmU7ZAINDw8WAh8AZWRkAhMPDxYCHwBlZGQCIQ9kFgJmD2QWAgIBD2QWBGYPDxYCHwAFFeeUouWTgeaXpeS6pOaYk+ihjOaDhWRkAgUPFCsAAmRkZBgBBSFjdGwwMCRjb250ZW50UGxhY2VIb2xkZXIkbGlzdFZpZXcPZ2TvwwhZn9o32kHbvt80R28pU8r4VMoPLXUMZYTs9agbMw==",
    "__VIEWSTATEGENERATOR": "A4896558",
    "__EVENTVALIDATION": "/wEdABBqSdC+vWTEina6fW+0pM+IQlnRBSjq2R0LFBhqvIaYOdWbMM2/DWJrZzd7rAbCDCMbHYsHDbD1wmtGXihvmsnJ8BlZTYOptctvPAnPr9y5LJoyUCbB5OTDc5yZRRQ2PEmkvfJ0YrSiHU+/oXyBv2VhrkJjLitQjF6ePtmGbXiLrIzHLqmP3vmfhBo4iiBYbOAMxUXSePoiAbW03Aek83lEONL/4qBgBPfx/RZlnlGK8F2urMXFZJUEVGioaQEN8wAcw2+N1zwrySGFt1o6Y654NdK0LUPG/u+ZYgXys7Q5MzRmtqZjr7cHdstuZRNzNiosHqM4wINIxgrfpUQJzv9gRYGyRknUe9l+gd4HsV/PcfBqIHmyKeIVq9A9Z+uNEnQ=",
    "ctl00$contentPlaceHolder$ucDateScope$rblDateScope": "D",
    "ctl00$contentPlaceHolder$ucSolarLunar$radlSolarLunar": "S",
    "ctl00$contentPlaceHolder$txtSTransDate": "106/11/28",
    "ctl00$contentPlaceHolder$txtETransDate": "106/11/28",
    "ctl00$contentPlaceHolder$txtMarket": "全部市場",
    "ctl00$contentPlaceHolder$hfldMarketNo": "ALL",
    "ctl00$contentPlaceHolder$txtProduct": "全部產品",
    "ctl00$contentPlaceHolder$hfldProductNo": "ALL",
    "ctl00$contentPlaceHolder$hfldProductType": "A",
    "__ASYNCPOST": "true",
    "ctl00$contentPlaceHolder$btnQuery": "查詢"
}''')
headers = json.loads(r'''{
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Length": "1647",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "_ga=GA1.3.826591586.1510195469; ASP.NET_SessionId=k5uy1m40d0d2j2mmrb3ipf3g",
    "Host": "amis.afa.gov.tw",
    "Origin": "http://amis.afa.gov.tw",
    "Referer": "http://amis.afa.gov.tw/fruit/FruitProdDayTransInfo.aspx",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    "X-MicrosoftAjax": "Delta=true",
    "X-Requested-With": "XMLHttpRequest"
}''')

for _day in range(1,1200):
    dt_to_crawl = today_dt - datetime.timedelta(days=_day)
    data['ctl00$contentPlaceHolder$txtSTransDate'] = gen_stransdate(dt_to_crawl)
    print('[INFO][%s] crawling %s'%(datetime.datetime.now().isoformat(), dt_to_crawl))
    resp = requests.post(url, data=data, headers=headers)
    with open('./fruit_data/%s.html'%(dt_to_crawl.isoformat()), 'w') as f:
        f.write(resp.text)
