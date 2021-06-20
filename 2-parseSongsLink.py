dosya = open("linksOfSongs.txt")
index = 1
sart = True
while sart:
    temp = open("links/" + str(index) + ".txt", "w")
    for i in range(100):
        line = dosya.readline()
        if line == '':
            dosya.close()
            temp.close()
            sart = False
            break
        temp.write(line)
    index += 1