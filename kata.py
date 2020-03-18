def all_is_digit(a_string):
    a_list = list(a_string)
    for i in a_list:
        if not i.isdigit():
            return False
    return True

def ignore_greate_than_1000(number_list):
    for i,token in enumerate(number_list):
        if int(token) > 1000:
            number_list[i] = 0
    return number_list

def clean_string(numbers):
    collection_string = ""
    for token in numbers:
        if token == "\n":
            collection_string += ","
        if token.isdigit() or token == ",":
            collection_string += token

    return collection_string

def to_integer(a_list):
    for i,token in enumerate(a_list):
        a_list[i] = int(token)
    return a_list

########## Helper functions on the top #####


def add(numbers):
    if numbers == "":
        return 0

    elif all_is_digit(numbers) and numbers.isdigit():
        return int(numbers)

    else:
        cleaned_string = clean_string(numbers)

        number_list = cleaned_string.split(",")
        number_list = to_integer(number_list)
        number_list = ignore_greate_than_1000(number_list)

        return sum(number_list)

