def CheckEven(number):
    if number%2==0:
        print("number is even")
    else:
        print("Number is odd")
def main():
    number=(int(input("Enter the number: ")))
    CheckEven(number)
if __name__=="__main__":
    main()
