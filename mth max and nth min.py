list1=[]
n=int(input("enter the no.of elements:"))
for i in range(n):
    a=int(input("enter the number:"))
    list1.append(a)
list2=list(set(list1))
list2.sort()
print(list2)
m=int(input("enter the mth maximum number"))
n=int(input("enter the nth minimum number:"))
print("mth largest number:",list2[-m])
print("nth minimum number:",list2[n])
print("sum=",list2[-m]+list2[n])
print("diff=",list2[-m]-list2[n])
