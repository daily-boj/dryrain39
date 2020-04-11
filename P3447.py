import sys

s = sys.stdin.read()
while "BUG" in s:
    s = s.replace("BUG", "")
print(s)
