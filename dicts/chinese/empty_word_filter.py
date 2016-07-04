#!/usr/bin/python3

f = open("fina.txt")

lines = f.readlines()

pt = True

for i in range(0,len(lines)):
	if lines[i].strip() == "---------------nn":
		pt = True
	if i + 3 < len(lines) and lines[i].strip() ==  lines[i+3].strip():
		pt = False
	if pt:
		print(lines[i].strip())
