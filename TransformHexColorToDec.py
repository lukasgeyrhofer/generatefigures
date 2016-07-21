#!/usr/bin/env python

import sys
import argparse

letters=['A','B','C','D','E','F']
digits=['0','1','2','3','4','5','6','7','8','9']
def lettertonumber(letter):
	if letter in digits:
		return int(letter)
	elif (letter=='a' or letter=='A'):
		return 10
	elif (letter=='b' or letter=='B'):
		return 11
	elif (letter=='c' or letter=='C'):
		return 12
	elif (letter=='d' or letter=='D'):
		return 13
	elif (letter=='e' or letter=='E'):
		return 14
	elif (letter=='f' or letter=='F'):
		return 15
	else:
		exit(1)

parser = argparse.ArgumentParser()
parser.add_argument("-c","--hexcolors",nargs = "*")
parser.add_argument("-N","--normalize",default=False,action="store_true")
args = parser.parse_args()

for colorhex in args.hexcolors:
    assert len(colorhex)==6,"failed"

    colordec1 = lettertonumber(colorhex[0])*16 + lettertonumber(colorhex[1])
    colordec2 = lettertonumber(colorhex[2])*16 + lettertonumber(colorhex[3])
    colordec3 = lettertonumber(colorhex[4])*16 + lettertonumber(colorhex[5])
    if args.normalize:
        print "{:.6f} {:.6f} {:.6f}".format(colordec1/255.,colordec2/255.,colordec3/255.)
    else:
        print "{:3d} {:3d} {:3d}".format(colordec1, colordec2, colordec3)

