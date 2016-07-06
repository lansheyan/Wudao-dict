#!/bin/python3

f = open("section.txt")

p_tag = False

lines = f.readlines()

cache = [""]

for line in lines:
	if line.strip() == "":
		continue
	if cache[-1].startswith("例句：") and line.strip() == "---------------nn":
		cache.remove(cache[-1])
		
	if line.strip() == "---------------nn":
		for v in cache:
			print(v)
		cache = [""]
		p_tag = True
	if(cache[-1] == "例句：") and (line.startswith("1. 百科") or line.startswith("1. 应用推荐")):
		cache.remove(cache[-1])
		p_tag = False
	
	elif p_tag == True:
		cache.append(line.strip())
		
