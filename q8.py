# 8. Write a recursive python function to print binary of a given decimal number.

def printBinary(n):
    if(n==0 or n==1):
        print(n%2,end='')
    else:    
        printBinary(n//2)
        print(n%2,end='')

printBinary(int(input("Enter a number to print it's binary number: ")))