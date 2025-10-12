from fns_4 import *

def call_and_logging(fn, *args):
    def create_logging_str(action_type: str):
        return f"fn '{fn.__name__}' {action_type}"

    print(create_logging_str('start'))

    result = fn(*args)

    print(create_logging_str('end'))

    return result

def do_anything(fn):
    return fn()

def create_incremental_fn():
    num = 0

    def increment():
        nonlocal num
        num += 1
        return num

    return increment