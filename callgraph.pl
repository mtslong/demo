#!/usr/bin/perl

#Josef's reply was extremely helpful, and with a lot of patience from #perl I have put together a script helps me filter out libraries I don't need in my call-graph.
#The script relies on telling callgrind to be extra verbose:
#valgrind --tool=callgrind --dump-instr=yes --compress-pos=no \
#  --compress-strings=no /opt/ats-trunk/bin/traffic_server
#This way it will produce strings instead of reference numbers, making it much easier parsable:
#

use Modern::Perl;
require File::Temp;

use strict;
use warnings;

my $cob = qr{^cob=/(?:usr/)?lib};
my $ob = qr{^ob=/(?:usr/)?lib/};
my $calls = qr{^calls=};

open (my $fh, '<', $ARGV[0]) or die $!;
my $tmp = File::Temp->new(UNLINK => 1);

## Skip all external libraries, as defined by $ob
while (readline $fh) {
    if (/$ob/ ) {
        # skip the entire ob= section we don't need.
        0 while defined($_ = readline $fh) && !/^ob=/;

        # put the last line back, we read too far
        seek($fh, -length($_), 1);
    } else {
        print $tmp $_;
    }
}
close ($fh);

## Skip all calls to external libraries, as defined by $cob
my $tmpname = $tmp->filename;
open ($tmp, '<', $tmpname) or die $!;
while (readline $tmp) {
    if (/$cob/) {

        # skip until we find a line starting with calls=
        # skip that line too
        0 while defined($_ = readline $tmp) && !/$calls/;

        # then we skip until we either hit ^word= or an empty line.
        # In other words: skip all lines that start with 0x
        0 while defined($_ = readline $tmp) && /^0x/;

        # put the last line back, we read too far
        seek($tmp, -length($_), 1);
    }  else {
       print;
    }
}
