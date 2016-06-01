#! /user/bin/perl
#use strict;


my @vDmin=qw(20160531.0000 20160531.0005 20160531.0010 20160531.0015 20160531.0020 20160531.0025 20160531.0030 20160531.0035 20160531.0040 20160531.0045 20160531.0050 20160531.0055);


foreach $tmp (@vDmin)
{
	print "$tmp \n";
	my $filepath="/var/data/stable/_CIF/".$tmp;
	$tmp =~ s/\.//;
	system "perl /home/etl/tmp/perl/TO_LTE_4G_USR.pl $tmp $filepath bitest02 371";
	`perl /home/etl/tmp/perl/TR_USR_IMSI.pl $tmp $filepath bitest02 &`;
}
