# =============================================================================
# FOR LOOP
# =============================================================================

for num in range(10):
    print(num)
    
    
for num1 in "hello world":
    print(num1)

sum=0    
for num2 in [1,2,3,4,5]:
    sum = sum+num2
    print(sum)

dict1 = {'k1':1,"k2":2,"k3":3}    
for num3,values in dict1.items():
    print(values)
    
for num4 in range(1,11,2):
    print(num4)
    
str_1 = "code warriors"
mylist=[]
for letter in str_1:
    mylist.append(letter)
    
my_list=[letter for letter in str_1]

list_2=[num**2 if num%2==0 else num**3 for num in range(0,11) ]


# =============================================================================
# WHILE LOOPS
# =============================================================================
num=0
while num<10:
    print(num)
    num=num+1
else:
    print("num is greater than or equal to 10")

num=0
while True:
    num = num+1
    if num==2:
        continue
    print(num)

while True:
    pass