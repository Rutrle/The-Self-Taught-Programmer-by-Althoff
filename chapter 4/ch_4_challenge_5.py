def convert_2_float(string):
    """
    Return float of string
    :param string: number in int or str
    :return: float(string)
    """
    try:
        return float(string)
    except ValueError:
        print('incorrect input, please enter a number')


# print(convert_2_float('something'))
