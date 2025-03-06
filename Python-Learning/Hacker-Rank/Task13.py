"""
A valid postal code  have to fullfil both below requirements:

 P must be a number in the range from 100000 to 999999 inclusive.
 P must not contain more than one alternating repetitive digit pair.
Alternating repetitive digits are digits which repeat immediately after the next digit. In other words, an alternating repetitive digit pair is formed by two equal digits that have just a single digit between them.

For example:

121426 # Here, 1 is an alternating repetitive digit.
523563 # Here, NO digit is an alternating repetitive digit.
552523 # Here, both 2 and 5 are alternating repetitive digits.
Your task is to provide two regular expressions regex_integer_in_range and regex_alternating_repetitive_digit_pair. Where:

regex_integer_in_range should match only integers range from 100000 to 999999  inclusive

regex_alternating_repetitive_digit_pair should find alternating repetitive digits pairs in a given string.
"""

import re

# Matches a 6-digit number from 100000 to 999999
regex_integer_in_range = r"^[1-9][0-9]{5}$"

# Finds alternating repetitive digit pairs
regex_alternating_repetitive_digit_pair = r"(?=(\d)\d\1)"

P = input().strip()

print(bool(re.match(regex_integer_in_range, P)) 
      and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)