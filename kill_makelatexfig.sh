#!/bin/bash

killid=`ps -a | awk '{if($4=="makeplots.sh")print(" "$1);if($4=="make_latexfig.s")print(" "$1);if($4=="pdflatex")print(" "$1);}'`
if [[ `echo $killid | wc -w` -eq 3 ]]
then
	kill -9 $killid
fi
