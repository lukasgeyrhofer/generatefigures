#!/bin/bash

#  Extract filename from argument
filename=$(basename "$1")
filename="${filename%.*}"

#  Use Inkscape to separate image from text
inkscape -z -C --file=$1 --export-pdf="$filename"-tmp-src.pdf --export-latex

#  Create temporary TeX source to recombine image and text
#    & use a texheader file if locally available
echo '\documentclass[10pt]{article}'		> "$filename"-tmp.tex
echo '\usepackage{amsmath,amsfonts}'		>>"$filename"-tmp.tex
echo '\usepackage{amssymb,amstext}'		>>"$filename"-tmp.tex
echo '\usepackage{mathrsfs}'			>>"$filename"-tmp.tex
echo '\usepackage{fullpage}'			>>"$filename"-tmp.tex
echo '\InputIfFileExists{texheader}{}{}'	>>"$filename"-tmp.tex
echo '\InputIfFileExists{/home/lukas/projects/generatefigures/notation}{}{}'    >>"$filename"-tmp.tex
echo '\InputIfFileExists{/home/lukas/projects/generatefigures/tangocolors}{}{}' >>"$filename"-tmp.tex
echo '\usepackage{graphicx}'			>>"$filename"-tmp.tex
echo '\usepackage{color}'			>>"$filename"-tmp.tex
echo '\pagestyle{empty}'			>>"$filename"-tmp.tex
echo '\begin{document}'				>>"$filename"-tmp.tex
echo '\def\svgwidth{'$2'\textwidth}'            >>"$filename"-tmp.tex
echo '\input{'"$filename"'-tmp-src.pdf_tex}'	>>"$filename"-tmp.tex
echo '\end{document}'				>>"$filename"-tmp.tex

#  Compile and crop final pdf image
pdflatex "$filename"-tmp.tex
pdfcrop "$filename"-tmp.pdf "$filename".pdf

#  Remove temporary files
rm *-tmp.tex *-tmp.pdf *-tmp-src.pdf *-tmp-src.pdf_tex *-tmp.aux *-tmp.log
