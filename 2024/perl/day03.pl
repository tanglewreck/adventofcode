#!/usr/bin/env perl


my $n_tokens=0;
my $sum=0;
my $token_prefix=qq(mul\(\d+,\d+\));

# open($fp, "../data/day_3_part_1") or die;
# open($fp, "../data/day_3_part_1_example") or die;
open($fp, "../data/day_3_part_2") or die;
# open($fp, "../data/day_3_part_2_example") or die;

while (<$fp>) {
    @matches = m/(mul\(\d+,\d+\))/g;
    $n_matches = $#matches+1;
    $n_tokens += $n_matches;
    for my $match (@matches) {
        ($a, $b) = ($match =~ m/mul\((\d+),(\d+)\)/);
        $sum += eval($a * $b);
    }
}

print("$n_tokens  $sum\n");

