# snake case -> car_color (ale nie tylko)
# --------------------------- (1) --------------------------
# Tworzenie zmiennych / obiektów
# Język typowany dynamicznie

a1 = 10
a1 = "ala"
a1 = []

from typing import Final  # type hints
a2 = 11
a3: Final[int] = 22
a3 = 44

# --------------------------- (2) --------------------------
# Typy danych

b1 = True
b2 = False
b3 = a2 > 10
print(a2 + True)  # a2 + 1
print(a2 + False) # a2 + 0

b4 = None

# print(a2 + None)

b5 = 3278463278346784364783264237846237846237846237842
b6 = 23.3
b7 = 10 + 4j

from fractions import Fraction
b8 = Fraction(12, 8)
print(b8)

b9 = Fraction(12, 5)

b10 = b8 + b9
print(b10)

from decimal import Decimal
b11 = Decimal('12.3')

b12 = 'ala'
b13 = "ala"

# string interpolation
b14 = f'Name: {b10}'
print(b14)

b15 = r'C:\User'
b16 = rf'C:\User\{b10}'
print(b15)
print(b16)

b17 = f'''
First line {b10}
Second line
'''

# Iterable
# list,
# tuple,
# range,
# dict,
# set,
# frozenset,
# namedtuple
# bytes,
# bytearray
# ...

# --------------------------- (3) --------------------------
# Pewne specjalne właściwości języka

c1 = '12'
c2 = 19

# print(c1 + c2)
print(c1 + str(c2))
print(f'{c1}{c2}')

print([1, 2, 3] == [1, 2, 3])
print([1, 2, 3] < [1, 2, 4])
print([1, 2, 3] > [1, 2, 4])

# print('20' - 5)
# print(int('ala'))

# DESTRUKTURYZACJA + MAGIA NAWIASOW
c5 = [11, 22, 33]
c5_1, c5_2, c5_3 = c5
print(c5_1)
print(c5_2)
print(c5_3)

c6 = (11, 22, 33)  # tuple
c7 = 11, 22, 33  # tuple
c7_1, c7_2, c7_3 = c7

c8 = {11, 22, 33}  # set
c8_1, c8_2, c8_3 = c8

# dict
person = {
    'name': 'ADAM',
    'age': 10
}
name, age = person
name, age = person

[(name_key, name_value), (age_key, age_value)] = person.items()
print(name_key)
print(name_value)
print(age_key)
print(age_value)

# Truthy / Falsy

if c6:
    pass

if not c6:
    pass



