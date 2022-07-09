import re
pattern = "ABCD"
if re.match(pattern,"ABCD"):
    print("match")
else:
    print("no match")
