# def power(base, exponent=2):  #1
#     return base ** exponent
# print(power(5))
# print(power(9, 6))
from cmath import rect


# def connect(host, port=3306, protocol='TCP'):  #2
#     print(f"Host: {host}, Port: {port}, Protocol: {protocol}")
# connect("localhost")
# connect("localhost", 9095)
# connect("localhost", 9095, "UDP")
# connect(host="192.1.1", protocol="UDP")
# connect("yaswanth", protocol="UDP")

# def func(age, name='Guest'):  #3
#     print(name, age)
# func(20)
# func(20, "Krishna")


# def discount_price(price, discount=10):
#     return price - (price * discount / 100)
# print(discount_price(1000))
# print(discount_price(1000, 20))

# def multiply_all(*args):  #s2
#     product = 1
#     for num in args:
#         product *= num
#     return product
# print("Q1:", multiply_all(2, 3, 4))#

# def display_tags(**kwargs):  #3
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# print("\nQ2:")
# display_tags(name="Krishna", age=20, city="Hyderabad")
# Q3. describe_person(name, *hobbies)

# def describe_person(name, *hobbies):  #4
#     print("Name:", name)
#     print("Hobbies:", hobbies)
# print("\nQ3:")
# describe_person("Krishna", "Reading", "Gaming", "Cycling")

def f(*args):
    print(type(args))
    print(f)
f=(1,2,3)


# def create_html_tag(tag, **attributes): #4
#     attrs = " ".join(f"{key}='{value}'" for key, value in attributes.items())
#     print(f"<{tag} {attrs}>")
# print("\nQ5:")
# create_html_tag('a', href='https://python.org', target='_blank')

# def mixed(a, b, *args, **kwargs):
#     print("a =", a)
#     print("b =", b)
#     print("args =", args)
#     print("kwargs =", kwargs)
# mixed(
#     10, 20, 30, 40, 50, 60,
#     name="Krishna",
#     city="Hyderabad"

# count=len
# my_list=[10,20,30,40,50]
# print(count(my_list))

# def run_twice(func,value):
#      return func(func,value)
# def add_(x):
#     return x+1
# print(run_twice(add_, 5))
#
# cube =lambda x:x**3
# print(cube(3))

# largest=lambda x,y:x if x > y else y
# print(largest(10,20))

# def even(n):
#     return n % 2 == 0

# even=lambda n: n % 2 == 0
# print(even(2))
# print(even(4))

# fruits = [(1,'banana'),(2,'apple'),(3, 'cherry')]
# fruits.sort(key=lambda x: x[1])
# print(fruits)
#
# def square(x):
#     return x * x
# result = lambda n: square(n)
# print(result(5))

# celsius = [0, 20, 30, 40]
# fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
# print(fahrenheit)

# words = ["Apple","banana","Cat","dog","Elephant"]
# result = list(filter(lambda word: word[0].isupper(), words))
# print(result)

# from functools import reduce
# numbers = [1, 2, 3, 4, 5]
# product = reduce(lambda x, y: x * y, numbers)
# print(p)
