import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r'\b(\w)(\w)', r'\2\1', line))