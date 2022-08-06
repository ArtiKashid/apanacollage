#write a python program to reverse the string using python
def reverse(str):
    str=str[::-1]
    return str
S=input("Enter the string:")
print("The original string is:",S)
print("The reserved string using slice operator is:",reverse(S))
