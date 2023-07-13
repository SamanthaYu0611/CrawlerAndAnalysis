import requests
from bs4 import BeautifulSoup
import json
from time import sleep
import xml.etree.ElementTree as ET
import re

def get_711_events():
    url = 'https://www.7-11.com.tw/readxml.aspx'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'https://www.7-11.com.tw/special/article_new.aspx?item=Event_E029',
        'Origin': 'https://www.7-11.com.tw',
        'Cookie': 'ApplicationGatewayAffinityCORS=f8275e479131a9de50a78454cec80a71; ApplicationGatewayAffinity=f8275e479131a9de50a78454cec80a71; ASP.NET_SessionId=solnag55j1oxvy4541j125js; _gcl_au=1.1.1880139496.1684991954; _ga=GA1.3.512250731.1684991954; _gid=GA1.3.867348576.1685241495; _gat=1',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Sec-Ch-Ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }                                                                                                                                                                                                                                                     

    payload = {
        'num': '0'
    }                   
    retry_count = 0
    while retry_count < 10:   # EC2 Ubuntu 請求有時候會失敗 重複發幾次又會成功 所以寫try exception 讓他每隔3秒請求一次 直到成功為止 上限10次
        try:
            response = requests.post(url, headers=headers, data=payload)
            xml_data = response.content

            # 解析 XML
            bd = ET.fromstring(xml_data)
            items = bd.iter('Item')   # iter: find all items
            events = []
            for item in items:

                title = item.find('APP_BannerTitle').text
                period = item.find('Period').text
                content = item.find('Content').text
                remark = item.find('Remark').text

                pattern =  r"<font.*?>|<\/font>"
                remark = str(remark)
                remark = re.sub( pattern , "", remark)
                
                if not title:
                    title = "無"
                if not period:
                    period = "無" 
                if not content:
                    content = "無"
                if not remark:
                    remark = "無" 
                
                event = {}
                event["title"] = title
                event["period"] =  period
                event["content"] = content
                event["remark"] = remark
                events.append(event)
                # print(event)
            return events
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            retry_count += 1
            if retry_count < 10:
                print("Retrying in 3 seconds...")
                sleep(3)            

if __name__ == "__main__":
    events = get_711_events()
    print(events)

    filename = "output_7-11.json"
    with open(filename, "w", encoding='utf-8') as file:
        file.write(json.dumps(events, ensure_ascii=False, indent=4))
