import requests
from bs4 import BeautifulSoup as bs

headers = { 'User-Agent': ( 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')}

i = 1
j = 1
soz = ""
sart = True
while sart:
    try:
        dosya = open("links/" + str(i) + ".txt")
    except:
        sart = False
        print("Hata11")
        break
    sarkilar = dosya.readlines()
    if sarkilar == '':
        dosya.close()
    else:
        print("Links File: " + str(i))
        try:
            for sarki in sarkilar:
                r = requests.get(sarki, headers=headers)
                if r.status_code != 200:
                    print("Hata33")
                else:
                    soz=""
                    soup = bs(r.content,'lxml')
                    lyrics = soup.find('div',{"class":"lyric-text margint20 marginb20"})
                    paragraflar = lyrics.findAll('p')
                    for parag in paragraflar:
                        for br in parag.find_all("br"):
                            br.replace_with("\n")
                        soz += "\n" + parag.text + "\n"
                    dataset = open("lyrics/" + str(j) + ".txt", "w")
                    dataset.write(soz)
                    dataset.close()
                    j += 1
        except:
            print("Hata22")
            dosya.close()
        i += 1