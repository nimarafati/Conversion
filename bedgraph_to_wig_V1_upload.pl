#!/usr/bin/perl
#use strict;
#use warnings;

my $usage = "Usage: $0 <infile.bedgraph> <size(in bp)> <column>\nNima Rafati 20161008\nnimarafati\@gmail.com";
my $infile = $ARGV[0] or die $usage;
my $step= $ARGV[1] or die $usage;
my $column=$ARGV[2] or die $usage;
open(IN,$infile) || die "Could not open $infile: $!\n";
print "track type=wiggle_0 name=\"$infile\" description=\"$infile\" visibility=full\n";
while(<IN>){
   chomp;
   next if (/^track/);
	chomp($_);
	@lineArr = split(/\t/,$_);
	$chr=$lineArr[0];
	$start=$lineArr[1];
	if($start==0){$start=1;}
	$data=$lineArr[$column-1];
   my $length = $end - $start;
    print "fixedStep chrom=$chr start=$start step=$step\n$data\n";
}
close(IN);
exit(0);