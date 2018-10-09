import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r'\b(A|a)+\b', 'argh', line, 1))