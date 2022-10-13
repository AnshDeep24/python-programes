x=int(input("enter the size of list"))
y= int(input("enter the size of sublist"))
list1=[]
sublist=[]
for i in range(x):
    for j in range(y):
        sublist.append(input())
    list1.append(sublist)
    sublist=[]
print (list1)
x=int(input ("enter the size of list"))
stu=[]
record=[]
for i in range(0,x):

    
    stu.append(input())
    stu.append(input())
    record.append(stu)
    stu = []

print(record)