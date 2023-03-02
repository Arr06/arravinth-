def sumsquare(l):
    odd=[]
    even=[]
    for items in l:
        if items%2==0:
            even.append(items)
        else:
            odd.append(items)
    square1=[]
    square2=[]
    t1=0
    t2=0
    for item in odd:
        square1.append(item**2)
    for item1 in even:
        square2.append(item**2)
    for i in range(0,len(square1)):
        total=t1+square[i]
    for i in range(0,len(square2)):
        total2=t2+square2[i]
    final_ans=[]
    for j in total,total2:
        final_ans.append(j)
    print(final_ans)
l=[]
n=int(input("enter the no.of elements:"))
for i in range(n):
    a=int(input("enter the number:"))
    l.append(a)
