import numpy as np

integers = np.array([1, 2, 3])

print(type(integers))

# list comprehension
# create a one d array from a list comprehension
# that produces even integers from 2 - 20

integers = np.array([x for x in range(2, 21, 2)])
print(integers)

# 2d array of integers

integers = np.array([[1, 2, 3], [4, 5, 6]])
print(integers)

# 2d array of floats

floats = np.array([0.0, 0.1, 0.2, 0.3, 0.4])
print(floats)

a = integers.dtype
b = integers.ndim
c = integers.shape
d = integers.size  # total number of elements

print()

for row in integers:
    print(row)
    for col in row:
        print(col, end=" ")

# the flat method allows us to iterate through all the rows

for i in integers.flat:
    print(i)


# exercise - create a 2d array of 5 integers using the random module
# and list comphrension print out dimension, shape, and size

import random

a = np.array(
    [
        [random.randint(1, 10) for x in range(5)],
        [random.randint(1, 10) for x in range(5)],
    ]
)

# using np random module is easier
b = np.array(np.random.randint(1, 10, size=(2, 5)))


# default are floating point values
c = np.zeros(5)
d = np.ones(5)
e = np.ones((2, 4), dtype=int)
f = np.full((3, 5), 13)
g = np.arange(5)
h = np.arange(5, 10)
i = np.arange(10, 1, -2)

print()

# creates evenly spaced numbers between upper and lower limit
print(np.linspace(0.0, 1.0, num=5))

# reshape method to change the dimension
array1 = np.arange(1, 21)


# has to have the same number of elements
array2 = array1.reshape(4, 5)

print(array1)
print(array2)

array3 = np.arange(1, 100001).reshape(4, 25000)
print(array3)

array4 = np.arange(1, 100001).reshape(100, 1000)
print(array4)

# changes the elements within the array
numbers = np.arange(1, 6)
numbers += 10
print(numbers)
print(numbers * 2)  # numbers * [2, 2, 2, 2, 2]
print(numbers ** 3)

# numbers is unchanged by the arithemetic operators
print(numbers)

# multiplying integer arrays wiht floating point arrays results in floating point
numbers2 = np.linspace(1.1, 5.5, 5)

print(numbers * numbers2)

# comparing arrays to get a t/f value - returns boolean
# have to have same number of elements to compare

print(numbers >= 13)
print(numbers2 > numbers)
print(numbers == numbers2)