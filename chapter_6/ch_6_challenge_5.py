

given_list = ["The", "fox", "jumped", "over", "the", "fence", "."]


created_string = " ".join(given_list)


#not needed, but general solution to these types of problems
while " ." in created_string:
    rest = created_string[created_string.index('.'):]

    created_string = created_string[:created_string.index('.')-1]+rest


print(created_string)
