
def count_character_occurences(word):
    count_dict = {}
    word = word.lower()

    for character in word:
        if character in count_dict:
            count_dict[character] += 1
        else:
            count_dict[character] = 1

    print(count_dict)


count_character_occurences('Panda')
