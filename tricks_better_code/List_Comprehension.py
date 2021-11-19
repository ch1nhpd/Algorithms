# List comprehension in Python is a compact way of creating a list from a sequence.
# It is a short way to create a new list.
# List comprehension is considerably faster than processing a list using the for loop.

s = 'hello!'
lst = [i for i in s]
print(type(lst)) # list
print(lst)

print('='*50)
squares = [i * i for i in range(11)]
print(squares)

print('='*50)
# It is also possible to make a list of tuples
numbers = [(i, i * i) for i in range(11)]
print(numbers)

print('='*50)
# Can be combined with if expression
even_numbers = [i for i in range(21) if i % 2 == 0]  # to generate even numbers list in range 0 to 21
print(even_numbers)

print('='*50)
# Flattening a 2D array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)

print('#'*50)
# flattening a 3D array
arr3D = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
         [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
         [[19, 20, 21], [22, 23, 24], [25, 26, 27]]]
flat_list = [number    for arr2D in arr3D     for row in arr2D     for number in row]
print(flat_list)


#exercise:
print('-exercise-'*5)
#1
list1 = [(i,1,i,i**2,i**3,i**4,i**5) for i in range(11)]
print(list1)

#2 Flatten the following list to a new list
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
newList = [[x,x[:3],y] for arr in countries for x,y in arr ]
print(newList)

#3 Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
# {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# {'country': 'NORWAY', 'city': 'OSLO'}]

rs3 = [{'country': country, 'city': city} for arr in countries for country,city in arr]
print(rs3)

#4 Change the following list of lists to a list of concatenated strings:

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# output
# ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
rs4 = [first+' '+second for arr in names for first,second in arr]
print(rs4)