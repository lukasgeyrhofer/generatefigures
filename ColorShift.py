#!/usr/bin/env python
# Lukas Geyrhofer, lukas.geyrhofer@gmx.at, 2014

import sys
import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("-c","--color",help="(in hex notation)",default="ff0000")
parser.add_argument("-n","--count",default=10,type=int)
parser.add_argument("-R","--reverse",help="reverse output",action='store_true',default=False)
parsergroup = parser.add_mutually_exclusive_group()
parsergroup.add_argument("-B","--black",help="increase to black (default: decrase to white)",action='store_false',default=True)
parsergroup.add_argument("-C","--color2",help="increase from color (option -c) to color2 (option -C)",default="ffffff")
args = parser.parse_args()


if not args.black:
  color2 = "000000"
else:
  color2 = args.color2


try:
  c1 = np.array((int(args.color[0:2],16)*1.,int(args.color[2:4],16)*1.,int(args.color[4:6],16)*1.))
  c2 = np.array((int(color2[0:2],16)*1.,int(color2[2:4],16)*1.,int(color2[4:6],16)*1.))
except:
  print >> sys.stderr,"argument is not a color"
  exit(1)

  
if args.reverse:
  startcolor = c2
  endcolor = c1
else:
  startcolor = c1
  endcolor = c2

for i in range(args.count+1):
  c = startcolor + i*(endcolor - startcolor)/(args.count)
  print "%02x%02x%02x"%(int(c[0]),int(c[1]),int(c[2]))

  
  
  