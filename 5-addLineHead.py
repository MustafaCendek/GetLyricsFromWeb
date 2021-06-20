output = open("output.txt",'w', encoding="utf-8")
f = open('Preprocessed.txt', 'r', encoding="utf-8")
for line in f.readlines():
    output.write(line + "$ ")
output.close()