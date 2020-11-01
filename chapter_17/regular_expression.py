import re

my_list = "Beautiful is better than ugly"

matches = re.findall('Beautiful', my_list)


print(matches)

matches_insensitive = re.findall('beautiful', my_list, re.IGNORECASE)

print(matches_insensitive)


zen = """Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

m = re.findall("^If", zen, re.MULTILINE)
print(m)

m = re.findall("idea.$", zen, re.MULTILINE)
print(m)


string = "Two too."

m = re.findall("t[wo]o", string, re.IGNORECASE)

print(m)
