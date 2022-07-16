################################################################################
#Write a Python Program to Reverse a Number:

################################################################################

no=int(input("Enter the number"))
rev=0
while(no>0):                                 #first iteration     #Second iter        #third iter
    digit=no%10                              #153%3=3               15%10=5             1%10=1
   # print("digit is",digit)
    rev=rev*10+digit                         # 0*10+3=3        3*10+5=35              35*10+1=351
    #print("rev is ",rev)
    no=no//10                                #153/10=15         15/10=1                1/10=0
    #print("no is",no)
    print("Reverse of number",rev)           #3                    35                    351
