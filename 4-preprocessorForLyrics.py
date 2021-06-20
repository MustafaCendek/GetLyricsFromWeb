import os

#header = " $$$BASLANGIC$$$ "
#endline = " $$$SATIR-SONU$$$ "
#footer = " $$$BITIS$$$ " + endline + endline

header = "$$$BASLANGIC$$$"
footer = "$$$BITIS$$$\n\n"
endline = "\n"
alfabe = "abcçdefgğhıijklmnoöprsştuüvyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"

dizin = os.getcwd()
girisKlasoru = dizin + "\\lyrics"
cikisKlasoru = dizin
cikisYolu = cikisKlasoru + "\\Preprocessed.txt"

#Çıktı dosyası oluşturma
cikti = open(cikisYolu,'w',encoding='utf-8')
#Giriş klasöründeki dosya isimlerini okuma
dosyalar = os.listdir(girisKlasoru)
#Okunan isimlerden dosyalara erişme
for dosya in dosyalar:
    #Erişilen 
    f  = open(girisKlasoru + "\\" + dosya,'r',encoding='utf-8')
    icerik = f.readlines()
    f.close()
    #Çıktı Üretme
    cikti.write(header + endline)
    for satir in icerik:
        #Satır boşsa çıktıya dahil etmemek için kontrol 
        if(satir != "" and satir !="\n" and satir !=" "):
            #Datasetteki I karakteri ve l karakteri sorununu düzeltme
            onceki = ''
            yeniSatir = ""
            for harf in satir:
                if (harf == 'I'):
                    if (onceki not in alfabe):
                        yeniSatir += harf
                    else:
                        yeniSatir += "l"
                else:
                    yeniSatir += harf
                onceki = harf
            #Datasetteki Boşluk sorunlarını düzeltme
            cikti.write(yeniSatir.strip() + endline)
    cikti.write(footer + endline)
cikti.close()