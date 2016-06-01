#!/usr/bin/env perl
#
use strict;

if(@ARGV != 1)
{
	print "Usage: $0 dirname\n";
	exit 1;
}

my ($dir) = @ARGV;

opendir(DIR, $dir) or die $!;

while(my $filename = readdir(DIR))
{
	next if ($filename =~ /^\./);
	print "$filename\n";
}

closedir DIR;
