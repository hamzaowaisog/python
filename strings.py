##Strings
str_1 = "code warriors"
str_2 = '100'
str_3 = str_1+str_2
print(str_3)

str_4 = "Python by "+str_1
print(str_4)

print("python by "+str_1)

print(len(str_1))

print(str_1[7])

for i in range(len(str_1)):
    print(str_1[i]+ " ",i)

print(str_1[-1])

print(str_1[2::2])

str_4 = str_4.split("o")


import string
import string
line1 =  "And Then There Were None"
line2 = "Famous In Love"
line3 = "Famous Were The Kol And Klaus"
line4 = line1+line2+line3
print(string.find(line1,'Were'),string.count((line4),'And'))
