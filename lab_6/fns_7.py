def check_can_format_to_number(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def get_hello():
    return "Hello World"

def add(a, b):
    return a + b