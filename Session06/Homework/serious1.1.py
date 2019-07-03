import requests
import bs4
import xlsxwriter

response=requests.get("https://www.apple.com/itunes/charts/songs/")
soup=bs4.BeautifulSoup(response.content.decode(),"html.parser")

section=soup.find("section",{"class":"section chart-grid"})
ul=section.div.ul
all_li=ul.find_all("li")

result=[]

for v in all_li:
    dic={
        "title": v.h3.a.string,
        "artist": v.h4.a.string
    }
    result.append(dic)

wb = xlsxwriter.Workbook("songs.xlsx")
ws = wb.add_worksheet()
r = 0
c = 0
for i in result:
    ws.write(r,c,i["title"])
    ws.write(r,c+1,i["artist"])
    r += 1
wb.close()
