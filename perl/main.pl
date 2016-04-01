#!/usr/bin/env perl

use strict;

sub echo
{
	print "hi, echo\n";
}

main:
{
	print "hi, main\n";
	&echo
}
