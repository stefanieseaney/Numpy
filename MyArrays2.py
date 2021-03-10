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


# 12 random grades in range 60- 100 then reshape result to 3 x 4 array
# calc average of all grades, average for each test and averages for each student

grade = np.random.randint(60, 101, 12).reshape(3, 4)


all_grades_avg = grade.mean()
each_test_avg = grade.mean(axis=0)
each_student_avg = grade.mean(axis=1)

print(all_grades_avg, each_test_avg, each_student_avg)


# shallow copy (view) - view of array and whatever changes in view affects array and vise versa
# not independent

numbers = np.arange(1, 6)

print(numbers)

numbers2 = numbers.view()

numbers[1] *= 10

print(numbers2)

# slice views

numbers2 = numbers2[0:3]

numbers[1] *= 20

print(numbers2)


# deep copy - independent from original and returns a new array with a deep copy of the original array
numbers = np.arange(1, 6)
numbers2 = numbers.copy()

numbers[1] *= 10

print(numbers)
print(numbers2)


grades = np.array([[87, 96, 70], [100, 87, 90]])

a = grades.reshape(1, 6)

print(grades)

print(a)

# reshape does not affect the original but resize does

b = grades.resize(1, 6)

print(grades)
print(b)


# flatten methods - produces a deep copy and does the same thing as reshape
flattened = grades.flatten()

# produces a shallow copy - raveled
raveled = grades.ravel()

raveled[0] = 100

print(grades)

raveled[5] = 99

print(grades)

# transpose the columns and rows
t = grades.T

print(t)
print(grades)

grades2 = np.array([[94, 77, 90], [100, 81, 82]])

# add more columns
h_grades = np.hstack((grades, grades2))

# adds more rows
v_grades = np.vstack((grades, grades2))

print(h_grades)
print(v_grades)