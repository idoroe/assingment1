def my_Mul(a,b):
    return a * b

def myDiv(a,b):
    return a //b

def validate_integer(input_str):
    if input_str.isdigit():
        return True, int(input_str)
    else:
        return False, None