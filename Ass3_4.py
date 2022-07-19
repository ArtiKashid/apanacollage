# ================================================================
# Write a program which accept N numbers from user and store it
# into List. Accept one another number from user and return
# frequency of that number from List.
# ================================================================
def Ifreq(imatch,list):
    icnt=0
    # Iterate the complete list till end
    for ino in list:
        # Compare each element and increment the matching count
        if (imatch==ino):
            icnt=icnt+1
    return icnt




def main():
    list=[]
    size=int(input("Enter size of list:"))
    for i in range(size):
        no=int(input("Enter elements in the list:"))
        list.append(no)
    print(list)
    imatch=int(input("Enter the value for frequency count:"))

    print("The frequency of {} value is : {}".format(imatch, Ifreq(imatch, list)))


if __name__=="__main__":
    main()