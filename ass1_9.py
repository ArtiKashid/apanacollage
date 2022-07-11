#Write a program which display first 10 even numbers on screen.
#Output :  2 4 6 8 10 12 14 16 18 20
def fun():
    for i in range(1,11):
        if i%2==0:
            print("even number is",i)

def main():
    fun()

if __name__=="__main__":
        main()