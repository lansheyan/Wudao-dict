

#f = open("section.txt","r")
#lines = f.readlines()
#co = len(lines)
#skip = False
#for i in range(0,co):
#	if lines[i].strip() == "---------------nn" and i + 3< co and lines[i+3].strip() == "添加释义":
#		skip = True
#	if lines[i] == "---------------nn":
#		skip = False
#	if not skip:
#		print(lines[i])


fp = open("section.txt", "r")
content = fp.readlines()
fp.close()

for idx in range(0, len(content)):
	content[idx] = content[idx].strip()

uncommit = ""
skip = False

for line in content:
	if len(line) == 0:
		continue
	if line == "---------------nn":
		if not skip:
			print(uncommit)
			print("---------------nn")
		uncommit = ""
		skip = False
		continue
	if line == "添加释义":
		skip = True
		continue
	
	uncommit += line + "\n"

