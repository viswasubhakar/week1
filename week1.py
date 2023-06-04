# question 1
a='hello'
b=[1,2,3,4,5,6,7,8,9,10]
c=1.4
d=(1,2,3,4)
# question 2
var1 = '' #str
var2 = '[ DS , ML , Python]' #string
var3 = [ 'DS', 'ML' , 'Python' ] #list
var4 = 1. #float

# question 3
# / --> is for normal division
# // --> is for division with out getting the decimal values
# % --> for getting reminder
# ** --> for power function
print(4/5)
print(4//5)
print(4%5)
print(4**5)

# question 4
for i in range(0,10):
    print(b[i])
x=50
y=10
while(x%y==0):
    print(int(x/y))
    break
lis=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,21,22,23,24,25]
for _ in lis:
    if(_%3==0):
        print(_)
# we can change mutable data types
# we cant change immutable data types
list1=[1,2,3,4]
tup1=(1,2,3)
list1[1]=5
print(list1)
tup1[1]=5
print(tup1)
