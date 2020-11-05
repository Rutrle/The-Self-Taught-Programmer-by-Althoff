import re

my_string = "Arizona 479, 501, 870. California 209, 213, 650"


matches = re.findall('\d*\d', my_string, re.IGNORECASE)

print(matches)
