#example
f = open("temp.txt",'r')
fileContent = f.read()
#manual...
f.close()

#better
# don't close because variable f free after context(function) end
with open("temp.txt",'r') as f:
    file_content = f.read()
    # manual...
