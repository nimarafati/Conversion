#!/usr/perl

###########################################################################
# NiRa 2020/04
# Feed genbank file to extract gene_name and gene_id/Entrez_id. The output 
# will be printed on screen.
# use: script file_name 
###########################################################################
$new=0;
open(inF,$ARGV[0]);
while(<inF>){
	$line = $_;
	chomp($line);
	@lineArr0=split("\t",$line);
	if($line =~ /^DEFINITION/){
		$new=1;
                $line=~ m/(DEFINITION)\s+.*(\(.*\)).*/;
                $gene_id = $2;
                $gene_id =~ s/\(//g;
		$gene_id =~ s/\)//g;
        }elsif($line =~ /^\s+\/locus_tag/){
		$line=~ m/.*=(.*)/;
		$gene_name = $1;
		$gene_name =~ s/\"//g;
#	}else{
#		$gene_name = "";
#		$gene_id = "";
	} 
	if($gene_name ne "" && $gene_id ne "" && $new == 1){
		print "$gene_name\t$gene_id\n";
		$new=0;
	}
}
