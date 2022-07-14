# ================================================================
# Write a program which accept one number from user and return
# its factorial
# ================================================================

def factorial(num):
    sum = 1

    for i in range(2, (num + 1)):

        sum = sum * i

    return sum


def main():
    no = int(input("Enter the number for factorial :"))
    print("factorial of number is",factorial(no))


if __name__ == "__main__":
    main()