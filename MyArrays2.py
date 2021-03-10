import numpy as np

grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])

# each row = student
# each column = test

a = grades.sum()
b = grades.min()
c = grades.max()
d = grades.mean()
e = grades.std()
f = grades.var()

# calculated based on 87, 100, 94, 100 aka average across all students for test 1, test 2, and test 3
# if it was axis 1 it would be average per student
g = grades.mean(axis=0)  # axis can be 0 or 1
print("Average of each test", g)

h = grades.mean(axis=1)
print("Average for each student", h)


numbers = np.array([1, 4, 9, 16, 25, 36])

sqrt = np.sqrt(numbers)
print(sqrt)

numbers2 = np.arange(1, 7) * 10

np_add = np.add(numbers, numbers2)

print(np_add)

np_multiply = np.multiply(numbers2, 5)

print(np_multiply)


numbers3 = numbers2.reshape(2, 3)

numbers4 = np.array([2, 4, 6])

np_multiply2 = np.multiply(numbers3, numbers4)
print(np_multiply2)


# indexing and slicing

grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])

# give it row first then column
a = grades[0, 1]

print(a)

# want to get the full row
b = grades[1]

print(b)

# upper limit isn't included if want to select multiple sequential rows using slice notation
c = grades[0:2]

print(c)

# select multiple non sequential rows you separate them by a comma
d = grades[[1, 3]]

print(d)

# all rows just the first column - aka test one for all students
e = grades[:, 0]

print(e)

# test one and three for all students
f = grades[:, [0, 2]]

print(f)