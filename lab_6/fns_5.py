from fns_6 import *

def secure_user_data(secured_data: list[str], **kwargs):
    data = []
    for key, value in kwargs.items():
        if key not in secured_data:
            data.append({key, value})

    return data

def call_action_fn(a=0, b=0, fn=add):
    return action(a, b, fn)

def apply_actions_to_number(number: int, *args):
    transformed_number = number
    for arg in args:
        transformed_number = arg(transformed_number)

    return transformed_number