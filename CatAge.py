#Given the below class:
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
while True:
    try:
        cat1 = Cat(input('Cat1 name: '), int(input('Cat1 age: ')))
        break
    except ValueError:
        print()
        print('Numbers only for age please.')
        print()

print()

while True:
    try:
        cat2 = Cat(input('Cat2 name: '), int(input('Cat2 age: ')))
        break
    except ValueError:
        print()
        print('Numbers only for age please.')
        print()

print()

while True:
    try:
        cat3 = Cat(input('Cat3 name: '), int(input('Cat3 age: ')))
        break
    except ValueError:
        print()
        print('Numbers only for age please.')
        print()

print()


# 2 Create a function that finds the oldest cat
def max_age():
    old = max(cat1.age, cat2.age, cat3.age)
    return old


def min_age():
    young = min(cat1.age, cat2.age, cat3.age)
    return young


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
if max_age() == cat1.age:
    print(f'The oldest cat is {cat1.name} and they are {cat1.age} years old.')
elif max_age() == cat2.age:
    print(f'The oldest cat is {cat2.name} and they are {cat2.age} years old.')
elif max_age() == cat3.age:
    print(f'The oldest cat is {cat3.name} and they are {cat3.age} years old.')

print()

if min_age() == cat1.age:
    print(
        f'The youngest cat is {cat1.name} and they are {cat1.age} years old.')
elif min_age() == cat2.age:
    print(
        f'The youngest cat is {cat2.name} and they are {cat2.age} years old.')
elif min_age() == cat3.age:
    print(
        f'The youngest cat is {cat3.name} and they are {cat3.age} years old.')
