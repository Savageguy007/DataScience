f = open("MyText.txt","r")
lines = f.readlines()
string=''+str(lines)
uniqueChar=''.join(set(string))
print("Total unique characters are : ",len(uniqueChar))
for i in range(len(uniqueChar)):
 if uniqueChar[i].isalpha():
    print(uniqueChar[i],'=',end='')
    print(string.count(uniqueChar[i]))
f.close()