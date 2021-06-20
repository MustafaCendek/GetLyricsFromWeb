import sys
f = open(sys.argv[1],"rt", encoding='utf-8')
vocab = open(sys.argv[2],"w",encoding='utf-8')
icerik = f.read()
f.close()
icerik2 = icerik
vocab.write("-----HARFLER-----\n")
harfler = sorted(set(icerik2))
for char in harfler:
    vocab.write(char + "\n")
icerik_split=icerik.split()
kelimeler = sorted(set(icerik_split))
vocab.write("-----KELİMELER-----\n")
for word in kelimeler:
    vocab.write(word + "\n")
vocab.close()