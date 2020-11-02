import re
t = "__one__ __two__ __three__"

found = re.findall("__.*?__", t)

for match in found:
    print(match)


found_greedy = re.findall("__.*__", t)

for match in found_greedy:
    print(match)
