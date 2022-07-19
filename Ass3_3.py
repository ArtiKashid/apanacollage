# ================================================================
# Write a program which accept N numbers from user and store it
# into List. Return Minimum number from that List.
# ================================================================
def Imin(list):
    imin=list[0]
    for i in list:
        if(imin > i):
            imin=i
    return imin
def main():
    list=[]
    size=int(input("Enter size of list:"))
    for i in range(size):
        no=int(input("Enter elements in the list:"))
        list.append(no)
    print(list)
    print("The minimum number in the list is:",Imin(list))
if __name__=="__main__":
    main()