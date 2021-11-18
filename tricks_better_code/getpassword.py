from getpass import getpass
username = input("username: ")
password = input("input pass: ")

#this same input pass on kali
passGetpass = getpass("getpass password: ")# only on cmd

print('done!')
print(username,password)
print(username,passGetpass)