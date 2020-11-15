
def ss(list, wanted):
    found = False
    for i in list:
        if i == wanted:
            found = True
            break

    return found


numbers = range(0, 100)

s1 = ss(numbers, 2)
s2 = ss(numbers, 500)
print(s1)
print(s2)
