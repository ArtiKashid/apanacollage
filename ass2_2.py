# Write a program which accept one number and display below pattern (if userdefined  input=5 then print like this)
#       *	 *	 *	 *	 *
#
#       *	 *	 *	 *	 *
#
#       *	 *	 *	 *	 *
#
#       *	 *	 *	 *	 *
#
#       *	 *	 *	 *	 *
# ================================================================
def Pattern(isize):
    for i in range(isize):
        for j in range(isize):
            print("*\t",end=" ")
        print("\n")

def main():
    iret=(int(input("Enter the number")))

    Pattern(iret)

if __name__=="__main__":
            main()