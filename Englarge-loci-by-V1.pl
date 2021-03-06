#!/usr/bin/perl
##This script enlarges the windows by input bp 
##Nima Rafati: 20140625
#
use Getopt::Long;
&GetOptions('w=i' =>\$windowSize, 'f=s' =>\$summaryLociFile);
my $contact = "nimarafati\@gmail.com";
my $usage = "Englarge-loci-by-V1.pl -w 5000 -f edgeR-results-Loci-summary.bed
-w size to enlarge 
-f summary loci file generated by Loci-info-summary-V2-with-Flags-to-set-Column.pl
$contact\n";
if($windowSize eq "" || $summaryLociFile eq "")
{
	print $usage;
	exit;
}
open(inF1,$summaryLociFile);
while(<inF1>)
{
        $cntr++;
        chomp($_);
        @lineArr=split("\t",$_);
	$chr=$lineArr[0];
	$start=$lineArr[1];
	$end=$lineArr[2]+$windowSize;
	$loci=$lineArr[4];
	if($lineArr[1]-$windowSize>=0)
	{
		$start=$start-$windowSize;
		print "$chr\t$start\t$end";
		foreach (my $k=3; $k<scalar(@lineArr);$k++)
		{
			print "\t$lineArr[$k]";
		}
	}
	else
	{
		$start=0;
		print "$chr\t$start\t$end";
		foreach (my $k=3; $k<scalar(@lineArr);$k++)
		{
			print "\t$lineArr[$k]";
		}
	}
	print "\t$lineArr[0]-$lineArr[1]-$lineArr[2]\n";
}
close inF1;
