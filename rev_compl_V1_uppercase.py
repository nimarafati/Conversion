from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import argparse 
import re

parser = argparse.ArgumentParser(description="This script generates reverse complementary sqeuence\n.")
parser.add_argument("-fa", "--fasta", help = "A fasta sequence is provided here.", action = "store")
parser.add_argument("-up", "--uppercase", help = "Convert sequence to uppercase.", action = "store_true")
args = parser.parse_args()

def make_rc_record(record):
#	"""Returns a new SeqRecord with the reverse complement sequence."""
	record = SeqRecord(seq = record.seq.reverse_complement(), id = "rc_" + record.id, description = "reverse complement")
	if args.uppercase:
		print(args.uppercase)
		record = record.upper()
	return record

print(args.fasta)
records = map(make_rc_record, SeqIO.parse(args.fasta, "fasta"))
SeqIO.write(records, "rev_comp_" + args.fasta, "fasta")
