

given_string = "Where now? Who now? When now?"


print(given_string.split("?"))

lst = []
while '?' in given_string:

    lst.append(given_string[:given_string.index('?')])
    given_string = given_string[1+given_string.index('?'):]
    print(given_string)

print(lst)
