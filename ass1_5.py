#Write a program which display 10(or user given input)to 1 on screen.
def displayNum(no):
    for i in range(no,0,-1):
        print(i)
def main():
    no=int(input("enter no"))
    displayNum(no)
if __name__=="__main__":
    main()