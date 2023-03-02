def is_reverse(s):
     str=""
     for i in s:
          str=i+str
     return str

s=input("enter the string:")
print("mirror image:",end="")
print(is_reverse(s))
