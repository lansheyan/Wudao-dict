#!/bin/bash

count=0
sum=`wc -l words.txt`

for var in `cat words.txt`
do
	./d $var>>section.txt
	sleep 1
	echo $var: >>section.txt
	echo ---------------\n\n  >>section.txt
	let count++
	echo Searching:$count/$sum
done

