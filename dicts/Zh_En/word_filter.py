f = open("webdict_with_freq.txt","r")

lines = f.readlines()
for line in lines:
    line = line.strip().split()
    if int(line[1]) > 1000:
        print(line[0])


