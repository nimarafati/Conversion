#!/usr/bin/python

########################################################
# NBIS 2020 - Sweden                                   #  
# nimarafati@gmail.com	                               #
# Please cite the script by referencing to github      #
# repository 					       #
########################################################
import argparse
import re 
import sys

parser = argparse.ArgumentParser(description = 'Extract infromation from attributes')
parser.add_argument('-gff', help = 'Specify a gff file.', action = 'store')
parser.add_argument('-arg', help = 'Provide attributes that you want to extract in qutation separated by comma', action = 'store', type = str)
args = parser.parse_args()
#print(args);sys.stdin.readline()
#args_list = args.arg.strip().split(",")
if len(sys.argv)<2:
	print('Please provide at least one argument to extract from attrubites')

args_list = args.arg.strip().split(",")
#my_args = args.arg.strip().split(',')

fh = open(args.gff, 'r')
#Define the input parameters
#NC_030986.1     RefSeq  region  1       6854980 .       +       .       ID=NC_030986.1:1..6854980;Dbxref=taxon:426428;Name=1;chromosome=1;forma-specialis=lycopersici;gbkey=Src;genome=chromosome;mol_type=genomic DNA;strain=4287
#NC_030986.1     RefSeq  gene    943     2400    .       -       .       ID=gene-FOXG_10826;Dbxref=GeneID:28952273;Name=FOXG_10826;end_range=2400,.;gbkey=Gene;gene_biotype=protein_coding;locus_tag=FOXG_10826;partial=true
for line in fh:
    cntr = 0
    line_list = line.strip().split('\t')
    if not line.startswith('#'):
        chromosome = line_list[0]
	feature = line_list[2]
        start = int(line_list[3]) - 1 
	end = line_list[4]
	strand = line_list[6]
	if feature == 'mRNA' or feature == 'transcript':
		attributes = line_list[8]
	        record = str(chromosome) +  '\t' + str(start) + '\t' + str(end) + '\t' +  str(strand) + '\t'
        	attributes_dict = dict(x.split("=") for x in attributes.split(";"))
		for i in args_list:
			if i in attributes_dict:
				record = record + '\t' + str(attributes_dict[i]) 
			else:
				record = record + '\t' + str('.')
		print(record)
