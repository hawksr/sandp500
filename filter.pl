

#!/usr/bin/perl -w

use strict;

my $num_of_params;

my $num_of_params = @ARGV;

if ($num_of_params < 0)
{
die ("not enough params!!!");
}


open(FILE, "< $ARGV[0].csv") || die "File not found";
my @lines = <FILE>;
close(FILE);

my @newlines;
foreach(@lines) {
    $_=~   s/"date","close","volume","open","high","low"/ /g;
    $_=~   s/date,close,volume,open,high,low/ /g;
     
    $_=~   s/^\n$//g;         
   $_ =~ s/"//g;
     $_= '' if  $_ =~ /^16:00/;
   push(@newlines,$_);
}

open(FILE, "> $ARGV[0].csv") || die "File not found";
print FILE @newlines;
close(FILE);

