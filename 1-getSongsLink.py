import requests
from bs4 import BeautifulSoup as bs

harfler = ["A","B","C","Ç","D","E","F","G","H","l","İ","J","K","L","M","N","O","Ö","P","Q","R","S","Ş","T","U","Ü","V","W","X","Y","Z"]
sanatcilar = []
sarkilar = []
site= 'https://www.sarkisozlerihd.com/'
headers = { 'User-Agent': ( 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')}

for harf in harfler:
    r = requests.get(site + "alfabe/?harf=" + harf, headers=headers)
    if r.status_code != 200:
        print("Hata")
    else:
        soup = bs(r.content,'lxml')
        singers = soup.findAll('div',{"class":"list-line margint10 clearfix"})
        for singer in singers:
            sanatcilar.append(singer.find('a').get("href"))

for sanatci in sanatcilar:
    r = requests.get(sanatci, headers=headers)
    if r.status_code !=200:
        print("Hata")
    else:
        soup = bs(r.content,'lxml')
        songs = soup.findAll('div',{"class":"list-line margint10 clearfix"})
        for song in songs:
            sarkilar.append(song.find('a').get("href"))

with open("linksOfSongs.txt", "w") as txt_file:
    for sarki in sarkilar:
        txt_file.write(sarki + "\n")
txt_file.close()

