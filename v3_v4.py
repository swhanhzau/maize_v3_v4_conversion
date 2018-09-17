# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 13:25:03 2018

@author: Steven Han
"""
import argparse
from itertools import islice
parser=argparse.ArgumentParser()
parser.add_argument('-v3','--v3gene',help='v3inputgenelist',metavar='')
parser.add_argument('-v4','--v4gene',help='v4inputgenelist',metavar='')
parser.add_argument('-r','--reference',help='v3_v4_gramene',metavar='')
parser.add_argument('-o','--output',help='outputfile',metavar='')
args=parser.parse_args()
v3=args.v3gene
v4=args.v4gene
gramene=args.reference
outputfile=args.output
if gramene and outputfile:
    d3=d4={}
    out=open(outputfile,'w')
    for i in islice(open(gramene),1,None):
        i=i.strip().split()
        d4[i[0]]=i[1]
        d3[i[1]]=i[0]
    if  v3 and v4:
        print('you should only input v3 OR v4 gene list')
    elif not (v3 or v4):
        print('where is your input')
    else:
        if v3:
            print('inputfile=v3genelist')
            for i in open(v3):
                i=i.strip()
                if i in d3:
                    print(i,d3[i],file=out,sep='\t')
        if v4:
            print('inputfile=v4genelist')
            for i in open(v4):
                i=i.strip()
                if i in d4:
                    print(i,d4[i],file=out,sep='\t')

                    
