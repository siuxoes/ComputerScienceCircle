__author__ = 'Siuxoes'

# stringInput = input()
# first = stringInput[0]
# last = stringInput[len(stringInput)-1]
# stringInput = stringInput[1:len(stringInput)-1]
# stringInput = last + stringInput + first
# print(stringInput)

# charInput = input()
# charInput = ord(charInput)
# if charInput != 90:
#     next = chr((charInput + 1))
# else:
#     next = chr(65)
# print(next)

# stringInput = str(input())
# first = stringInput[0]
# stringInput = stringInput[1:len(stringInput)] + first + "ay"
# print(stringInput)

name = str(input())
nameWithoutFirst = name[1:len(name)]
nameWithB = "b"+nameWithoutFirst
nameWithF = "f"+nameWithoutFirst
nameWithM = "m"+nameWithoutFirst

print(name+", "+name+", "+"bo-"+nameWithB)
print("banana-fana fo-"+nameWithF)
print("fee-fi-mo-"+nameWithM)
print(name+"!")