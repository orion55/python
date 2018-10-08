import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    result = re.findall(r'cat', line)
    if len(result) >= 2:
        print(line)
