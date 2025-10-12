from fns_7 import *

def action(a=0, b=0, fn=add):
    return fn(a, b)

def get_new_user_string(name: str, age: int) -> str:
    return f"Новый участник {name}, возраст {age}"

def get_average_value(*args):
    return sum(args) / len(args)