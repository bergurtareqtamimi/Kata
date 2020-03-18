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

def contains_negative(numbers):
    for i in numbers:
        if i == "-":
            return True
    return False

def collect_negative(numbers):
    coll_str = ""
    for i,token in enumerate(numbers):
        if token == "-" and numbers[i+1].isdigit():
            coll_str += token+numbers[i+1]+","
    
    coll_str = coll_str[:-1]
    return coll_str

########## Helper functions on the top #####


def add(numbers):
    if numbers == "":
        return 0

    elif all_is_digit(numbers) and numbers.isdigit():
        return int(numbers)

    elif contains_negative(numbers):
        negatives = collect_negative(numbers)
        return "Negatives not allowed: "+negatives

    else:
        cleaned_string = clean_string(numbers)

        number_list = cleaned_string.split(",")
        number_list = to_integer(number_list)
        number_list = ignore_greate_than_1000(number_list)

        return sum(number_list)

