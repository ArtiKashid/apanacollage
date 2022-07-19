# ================================================================
# Write a program which accept N numbers from user and store it
# into List. Return Maximum number from that List
# ================================================================
def Imax(list):
    imaximum=list[0]
    for i in list:
        if (imaximum<i):
            imaximum=i
    return imaximum

def main():
    list=[]
    isize=int(input("Enter the number of elements to be entered:"))
    for i in range(isize):
        ino=int(input("Enter the elements in the list"))
        list.append(ino)
        print(list)
        print("The maximum number in the list is:",Imax(list))

if __name__=="__main__":
    main()