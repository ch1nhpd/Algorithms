a, b, c = (1, 2, 3)
d, e, _ = (1, 2, 3)
f, *j = (1, 2, 3, 4)
k, *l, m = (1, 2, 3, 4, 5)
n, *_ = (1, 2, 3, 4, 5, 6)

print(a)
print(b)
print(c)
print("d,e:", d, e)
print("f: ", f)
print('j: ', j)
print(f'k: {k}')
print('l: ', l)
print('m: ', m)
print('n: ', n)

def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # 15
