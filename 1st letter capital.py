def firstletter(word):
    if word.isalpha():
        s = word[0].upper() + '.'
        return s
    else:
        return ""   
sentence = input("enter the sentence:")
list = sentence.split()
s = ""
for word in list:
    s = s+ firstletter(word)
print(s)
