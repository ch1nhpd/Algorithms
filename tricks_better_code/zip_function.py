names = ['peter','alex','calos','wiener']
classs = ['C01','B01','D03','X11']
address = ['Vietnam','England','US','China']

#best code
for name,cla,add in zip(names,classs,address):
    print(f'{name} in class {cla} come from {add}')
for value in zip(names,classs,address):
    print(value)