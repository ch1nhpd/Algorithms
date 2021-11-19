#syntax
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3))

# Self invoking lambda function
print((lambda a, b: a + b)(2,3))

# Lambda Function Inside Another Function
def power(x):
    return lambda n : x ** n
cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets
print(cube)  #8