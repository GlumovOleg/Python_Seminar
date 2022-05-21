from fractions import Fraction

def rac_nums(a,b,action):
    if action == '*':
        x = int(a) * int(b)
        return x
    if action == '/':
        x = int(a) / int(b)
        return x
    if action == '+':
        x = int(a) + int(b)
        return x
    if action == '-':
        x = int(a) - int(b)
        return x
