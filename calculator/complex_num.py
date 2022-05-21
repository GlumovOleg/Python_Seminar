
def complex_nums(x, y, action):
    a = x.replace('j', '')
    a = complex(int(a[0]), int(a[2]))
    b = y.replace('j', '')
    b = complex(int(b[0]), int(b[2]))
    if action == '+':
        return a + b
    elif action == '-':
        return a - b
    elif action == '*':
        return a * b
    elif action == '/':
        return a / b
    else:
        print('Ошибка ввода данных')