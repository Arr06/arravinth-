l1=[]
l2=[]
a=0
b=0

while True:
    n=int(input("enter the number:"))
    if n==-1:
        break
    elif n>0:
        l1.append(n)
    elif n<0:
        l2.append(n)
for i in l1:
    a+=i
for j in l2:
    b+=i

c=a/len(l1)
d=b/len(l2)
print("the average negative number is:",c)
print ("the average positive number is:",d)
