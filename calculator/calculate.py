def str_in_list(string):
    string = string.split()
    list_result = [int(item) for item in string]
    return list_result


def complex_result(list_num):
    return complex(list_num[0], list_num[1])


def result(symbol, a, b):
    if symbol == '*':
        return a * b

    elif symbol == '/':
        return a / b

    elif symbol == '+':
        return a + b

    elif symbol == '-':
        return a - b
