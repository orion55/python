import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r'((\w)\2+)', r'\2', line))