import sys
f = open(sys.argv[1],"rt", encoding='utf-8')
icerik = f.read()
harfSayisi = len(icerik)
essizHarfSayisi = len(set(icerik))
icerik_split=icerik.split()
kelimeSayisi = len(icerik_split)
kelimeler = sorted(set(icerik_split))
essizKelimeSayisi = len(kelimeler)
satirsayisi = len(icerik.split("\n"))
lyricSayisi = len(icerik.split("$ $$$BASLANGIC$$$"))
print("Harf Sayısı:\t", f'{harfSayisi:,}')
print("Kelime Sayısı:\t", f'{kelimeSayisi:,}')
print("Satir Sayısı:\t", f'{satirsayisi:,}')
print("Lyric Sayısı:\t", f'{lyricSayisi:,}')
print("Eşsiz H Sayısı:\t", f'{essizHarfSayisi:,}')
print("Eşsiz K Sayısı:\t", f'{essizKelimeSayisi:,}')

try:
    result = open(sys.argv[2],"w",encoding="utf-8")
    result.write("Harf Sayısı:\t" + f'{harfSayisi:,}' + "\n")
    result.write("Kelime Sayısı:\t"+ f'{kelimeSayisi:,}'+"\n")
    result.write("Satir Sayısı:\t"+ f'{satirsayisi:,}'+"\n")
    result.write("Lyric Sayısı:\t"+ f'{lyricSayisi:,}'+"\n")
    result.write("Eşsiz H Sayısı:\t"+ f'{essizHarfSayisi:,}'+"\n")
    result.write("Eşsiz K Sayısı:\t"+ f'{essizKelimeSayisi:,}'+"\n")
    f.close()
except IndexError:
    f.close()