#!/bin/bash

for plotfile in `ls *.gnuplot`
do
	echo "gnuplot" $plotfile
	gnuplot $plotfile
done

if [[ -f *.eps ]]
then
    for epsfile in `ls *.eps`
    do
            echo "eps" $epsfile
            epstopdf $epsfile
    done
fi

if [[ -f *.svg ]]
then
    for svgfile in `ls *.svg`
    do
            echo "svg" $svgfile
            logfile=`echo $svgfile | sed 's/\.svg/\.log/g'`
            make_latexfig.sh $svgfile $1 > $logfile
    done
fi
