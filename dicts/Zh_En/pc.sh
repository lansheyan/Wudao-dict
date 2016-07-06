#!/bin/bash
count=0
sum=`wc -l words.txt`

for var in `cat words.txt`
do
	sleep 0.5
	echo $var: >>section.txt
	./dz $var>>section.txt
	echo ---------------\n\n  >>section.txt
	let count++
	echo Searching:$count/$sum
done
