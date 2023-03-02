uppercase_count=0
lowercase_count=0
number_count=0

while True:
    char=input("enter a character:")
    if char=='*':
        break
    if char.isupper():
        uppercase_count+=1
    elif char.islower():
        lowercase_count+=1
    elif char.isdigit():
        number_count+=1

print("number of uppercase characters:",uppercase_count)
print("number of lowercase characters:",lowercase_count)
print("the number count:",number_count)
