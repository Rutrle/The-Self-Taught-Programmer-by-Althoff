import re

my_string = "The ghost that says boo haunts the loo"


matches = re.findall('.oo', my_string, re.IGNORECASE)

print(matches)
