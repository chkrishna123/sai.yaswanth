# l=[1,7,8,12,14,21,22,63,66]
# m=list(map(lambda x:x**3,l))
# k=list(filter(lambda x:x%4,m))
# print(k)

# l=[1,7,8,12,14,21,22,63,66]
# m=(list(filter(lambda x:x%4,map(lambda x:x**3,l))))
# print(m)
#
# from functools import reduce
# l=[1,2,3,4,5,6,7,8,9,10]
# m=reduce(lambda x,y:x+y,l)
# print(m)
#
# from functools import reduce
# l = [1, 7, 6, 3, 8, 9, 11, 10]
# m = reduce(lambda x, y: x if x > y else y, l)
# print(m)
#
# c=[0,22,31,35,23]
# m=list(map(lambda x:(9/5*x)+32,c))
# k=list(filter(lambda x:x%3,m))
# print(k)

# a=1
# b=5
# sum=0
# c=0
# for i in range (a,b+1):
#     if(i%2==0):
#         sum=sum+i
#         c=c+1
# avg=sum/c
# print(avg)

# Two lists   #1
# a = [1, 2, 3, 4]
# b = [10, 20, 30, 40]
# # Using map() with lambda
# result = list(map(lambda x, y: x + y, a, b))
# # Print the result
# print(result)

#  Given list  #2
# nums = [12, 15, 7, 18, 20, 21, 25]
# result = list(filter(lambda x: (x % 3 == 0 or x % 5 == 0) and not
# (x % 3 == 0 and x % 5 == 0),nums))
# print(result)


# from functools import reduce  #3
# nums = [1, 2, 3, 4]
# result = reduce(lambda x, y: x + y, nums, 10)
# print(result)


# def say_hello():  #1
#     print("Welcome to Python!")
# say_hello()

# def add(a, b):   #2
#     return a + b
# result = add(5, 3)
# print(result)

# def test_function():  #3
#     print("This function has no return statement")
# result = test_function()
# print(result)

# def area_of_rectangle(length, width):  #4
#     return length * width
# area = area_of_rectangle(6, 4)
# print(area)

# def multiply(a, b, c):   #s1
#     return a * b * c
# print(multiply(2, 3, 4))

# def describe_pet(animal, name):   #S2
#     print(f"My {animal} is named {name}.")
# describe_pet("dog", "MAX")


# def add_numbers(a, b):  #s3
#     return a + b
# print(add_numbers(6))

# def power(base, exponent):   #s4
#     return base ** exponent
# print(power(2, 3))

# def full_name(first, middle, last):  #s
#     return first + " " + middle + " " + last
# print(full_name("Krishna", "Sai", "yaswanth"))








