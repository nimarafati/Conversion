#!/usr/perl

###########################################################################
# NiRa 2020/04
# Feed genbank file to extract gene_name and gene_id/Entrez_id. The output 
# will be printed on screen.
# use: script file_name 
###########################################################################

open(inF,$ARGV[0]);
while(<inF>){
	$line = $_;
	chomp($line);
	@lineArr0=split("\t",$line);
	if($line =~ /^\s+\/locus_tag/){
		$line=~ m/.*=(.*)/;
		$gene_name = $1;
		$gene_name =~ s/\"//g;
	}elsif($line =~ /^\s+\/DEFINITION=/){
		$line=~ m/.*:(.*)/;
		$gene_id = $1;
		$gene_id =~ s/\"//g;
	}else{
		$gene_name = "";
		$gene_id = "";
	} 
	if($gene_name ne "" && $gene_id ne ""){
		print "$gene_name\t$gene_id\n";
	}
}
