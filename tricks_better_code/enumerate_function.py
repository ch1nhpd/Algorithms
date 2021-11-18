#bad code
names = ['peter','alex','calos','wiener']
i = 1
for name in names:
    print(i,name)
    i+=1

#best code use enumerate
for (i,name) in enumerate(names,start=1):
    print(i,name)