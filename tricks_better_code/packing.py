# list
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s


print(sum_all(1, 2, 3))  # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7))  # 28


# Packing Dictionaries
def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
    # Printing dictionary items
    for key in kwargs:
        print("{key} = {kwargs[key]}")
    return kwargs


print(packing_person_info(name="Asabeneh",
                          country="Finland", city="Helsinki", age=250))
