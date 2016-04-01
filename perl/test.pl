#!/usr/bin/env perl
use strict;
require "/home/montella/perl/a.pl";

die $! if (@ARGV != 1);

open (OH, "$ARGV[0]") or die $!;

while(<OH>)
{
	print if 1..10;
}
close OH;

print "test requied\n";
test();
