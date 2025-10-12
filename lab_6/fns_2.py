from fns_3 import *

def multiply(first_num):
    def times(second_num):
        return first_num * second_num

    return times

def create_message(text):
    def message(name):
        return f"{text} {name}"

    return message

def split_value(params, separator):
    if type(params) is not str:
        raise TypeError("params must be a string")

    return params.split(separator)