import requests
from bs4 import BeautifulSoup
import json
def get_family_events():

    url = 'https://www.family.com.tw/Marketing/Event#all'

    headers = {
        'Authority': 'www.family.com.tw',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Cookie': '_ga=GA1.1.699740583.1684992307; _ga_6W05QWWLX4=GS1.1.1685352272.1.0.1685352274.0.0.0; _ga_2R291J60D2=GS1.1.1685352347.1.0.1685352352.0.0.0; _ga_KBLNFSSS3J=GS1.1.1685351716.5.1.1685352465.0.0.0; _ga_5WDPCFC7XG=GS1.1.1685351716.5.1.1685352465.0.0.0',
        'Referer': 'https://www.family.com.tw/Marketing/',
        'Sec-Ch-Ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    tab = soup.find(id="all")
    cards = tab.findAll(class_="card card--event")


    events = []
    for card in cards:

        title = card.find(class_="card__title").text.strip()
        period = card.find(class_="card__date").text.strip()
        content = card.find(class_="card__text line-clamp").text.strip()
        label = card.find(class_="card__label").text.strip()
        
        if not title:
            title = "無"
        if not period:
            period = "無"
        if not content:
            content = "無"
        if not label:
            label = "無"
                
        event = {}
        event["title"] = title
        event["period"] = period
        event["content"] = content
        event["label"] =  label
        events.append(event)
        # print(event)
    return events

if __name__ == "__main__":
    events = get_family_events()
    print(events)

    filename = "output_family.json"
    with open(filename, "w", encoding='utf-8') as file:
        file.write(json.dumps(events, ensure_ascii=False, indent=4))
