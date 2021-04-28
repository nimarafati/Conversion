#!/usr/bin/python

########################################################
# 2021 		                                       #  
# nimarafati@gmail.com                                 #
# Please cite the script by referencing to github      #
# repository                                           #
########################################################
import argparse
import re
import sys
from Bio import SeqIO

parser = argparse.ArgumentParser(description = 'Convert gbk forat to Fasta')
parser.add_argument('-gbk', help='A file with genbank format as input', action = 'store')
parser.add_argument('-output', help = 'save the sequences in a fasta format', action = 'store')
args = parser.parse_args()

SeqIO.convert(args.gbk, "genbank", args.output, "fasta")
