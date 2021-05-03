########################################################
# nimarafati@gmail.com	                               #
# Please cite the script by referencing to github      #
# repository 					       #
########################################################
import argparse
import re
import sys
import os
import pandas

parser = argparse.ArgumentParser(description="This script matches IDs from key file and gff/gtf file.")
parser.add_argument("--key_file", "-key", help = "A key file consists of IDs")
parser.add_argument("--gff_file", "-g", help = "gff file")
parser.add_argument("--target_ID", "-i", help = "target ID to use for replacing in gff file")
parser.add_argument("--output", "-o", help = "Output file")

args=parser.parse_args()

key_dict = {}
keys = open(args.key_file, 'r') 
keys.df = pd.DataFrame(data=keys)
print(keys.df)

#for line in keys:
#    print(line)
#    sys.exit()
