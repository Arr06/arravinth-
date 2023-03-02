list1=[]
n=int(input("enter the no.of elements:"))
for i in range(n):
    a=int(input("enter the number:"))
    list1.append(a)
list2=list(set(list1))
list2.sort()
print(list2)
target=int(input("enter the target number:"))
for j in range(len(list2)):
    for k in range(j+1,len(list2)):
        if list2[j]+list2[k]==target:
            print(list2[j],"+",list2[k],"=",target)
