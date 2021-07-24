import urllib.request as req
import bs4
from color import colorprint
import re

python = []
app = []
html = []
game = []
none = []

def getData(url):
    request=req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.70",
        "cookie":"over18=1"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    root = bs4.BeautifulSoup(data, "html.parser")
    titles=root.find_all("div",class_="List_wrap__cdr1L")

    price = root.find("span",class_="List_money__36l3t")
    price = root.find_all("div",class_="List_price__12lqR")
    num=0
    for title in titles:
        
        if title.a.string.find("Python") != -1:
            python.append(title.a.string)
            try:
                regex = re.compile(r'\d+,\d+')
                match = regex.findall(price[num].text)
                python.append("價格:" + match[0] + " ~ " +match[1])
            except:
                try:
                    regex = re.compile(r'\d+')
                    match = regex.findall(price[num].text)
                    python.append("價格:" + match[0] + " ~ " +match[1])
                except:
                    python.append("無法取得價位")
            python.append("https://top.104.com.tw" + title.a.get("href"))
        elif title.a.string.find("Unity") != -1:
            game.append(title.a.string)
            try:
                regex = re.compile(r'\d+,\d+')
                match = regex.findall(price[num].text)
                game.append("價格:" + match[0] + " ~ " +match[1])
            except:
                try:
                    regex = re.compile(r'\d+')
                    match = regex.findall(price[num].text)
                    game.append("價格:" + match[0] + " ~ " +match[1])
                except:
                    game.append("無法取得價位")
            game.append("https://top.104.com.tw" + title.a.get("href"))
        elif title.a.string.find("APP") != -1:
            app.append(title.a.string)
            try:
                regex = re.compile(r'\d+,\d+')
                match = regex.findall(price[num].text)
                app.append("價格:" + match[0] + " ~ " +match[1])
            except:
                try:
                    regex = re.compile(r'\d+')
                    match = regex.findall(price[num].text)
                    app.append("價格:" + match[0] + " ~ " +match[1])
                except:
                    app.append("無法取得價位")
            app.append("https://top.104.com.tw" + title.a.get("href"))
        elif title.a.string.find("前端") != -1:
            html.append(title.a.string)
            try:
                regex = re.compile(r'\d+,\d+')
                match = regex.findall(price[num].text)
                html.append("價格:" + match[0] + " ~ " +match[1])
            except:
                try:
                    regex = re.compile(r'\d+')
                    match = regex.findall(price[num].text)
                    html.append("價格:" + match[0] + " ~ " +match[1])
                except:
                    html.append("無法取得價位")
            html.append("https://top.104.com.tw" + title.a.get("href"))
        elif title.a.string.find("網站") != -1:
            html.append(title.a.string)
            try:
                regex = re.compile(r'\d+,\d+')
                match = regex.findall(price[num].text)
                html.append("價格:" + match[0] + " ~ " +match[1])
            except:
                try:
                    regex = re.compile(r'\d+')
                    match = regex.findall(price[num].text)
                    html.append("價格:" + match[0] + " ~ " +match[1])
                except:
                    html.append("無法取得價位")
            html.append("https://top.104.com.tw" + title.a.get("href"))
        elif title.a.string.find("遊戲") != -1:
            game.append(title.a.string)
            try:
                regex = re.compile(r'\d+,\d+')
                match = regex.findall(price[num].text)
                game.append("價格:" + match[0] + " ~ " +match[1])
            except:
                try:
                    regex = re.compile(r'\d+')
                    match = regex.findall(price[num].text)
                    game.append("價格:" + match[0] + " ~ " +match[1])
                except:
                    game.append("無法取得價位")
            game.append("https://top.104.com.tw" + title.a.get("href"))
        else:
            none.append(title.a.string)
        
        
        num+=1
   
#print list

def allprint(listtype,):
    print("----------"+ listtype +"-----------")
    if listtype == "Python":
        for item in python:
            colorprint("blue",item)
    if listtype == "None":
        for item in none:
            colorprint("white",item)
    if listtype == "Game":
        for item in game:
            colorprint("green",item)
    if listtype == "Html":
        for item in html:
            colorprint("perple",item)
    if listtype == "App":
        for item in app:
            colorprint("red",item)

count = 20
getData("https://top.104.com.tw/caseList?cats=4004000&pageNum=1")
for i in range(count-1):
    getData("https://top.104.com.tw/caseList?cats=4004000&pageNum="+ str(i+2) + "")

allprint("None")
allprint("App")
allprint("Game")
allprint("Html")
allprint("Python")
