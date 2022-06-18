while True:
    try:
        a = input('Enter a number for a: ')
        print()
        a = float(a)
        break
    except ValueError:
        print('Numbers only please.')

a_squared = round(a**2, 2)
print(f'a\u00b2 = {a_squared}')
print()

while True:
    try:
        b = input('Enter a number for b: ')
        print()
        b = float(b)
        break
    except ValueError:
        print('Numbers only please.')

b_squared = round(b**2, 2)
print(f'b\u00b2 = {b_squared}')
print()

c_squared = a_squared + b_squared

print(f'{a_squared} + {b_squared} = {c_squared}')
print()
print(f'c\u00b2 = {c_squared}')
print()

c = c_squared**.5
print(f'c = {round(c, 1)}')
