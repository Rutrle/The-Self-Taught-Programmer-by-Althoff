import re

my_list = "Beautiful is better than ugly"

matches = re.findall('Beautiful', my_list)


print(matches)

matches_insensitive = re.findall('beautiful', my_list, re.IGNORECASE)

print(matches_insensitive)
