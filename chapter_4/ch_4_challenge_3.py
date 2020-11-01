def multi_printer(var_1, var_2, var_3, var_4='', var_5=''):
    """
    Prints all parameters
    :param var_1: string, int or float
    :param var_2: string, int or float
    :param var_3: string, int or float
    :optional param var_4: string, int or float
    :optional param var_5: string, int or float

    """
    print(f'{var_1}, {var_2}, {var_3}, {var_4}, {var_5}')


multi_printer('something', 'second_arg', 'third_arg', var_5='fifth_arg')
