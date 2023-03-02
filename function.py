'''def student(name,age,*marks):
    print(name,age,marks)
student("ravi",25,"marks=",100,99,98,97,95)'''

n=int(input("enter the number:"))
factors=[]
s=0
for i in range(1,n):
    if(n%i==0):
        factors.append(i)
print(factors)
for j in range(0,n):
    s+=1
print("sum:",s)
if(s==n):
    print("perfect number")

'''l=[]
b=1
n=int(input("enter the no.of elements:"))
for i in range(n):
          a=int(input("enter the number:"))
          l.append(a)

print(l)
for j in l:
      b=j*b
print("total:",b)

def testnum(n):
    if n in range(-3,10):
        print ("the number falls in range")
    else:
        ("the number is outside the loop:")

n=int(input("enter the number"))
testnum(n)'''

      

      
      
    
