def convert_2_float(string):
    try:
        return float(string)
    except ValueError:
        print('incorrect input, please enter a number')


#print(convert_2_float('ddd5'))
