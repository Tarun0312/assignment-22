# 9. Write a recursive python function to print octal of a given decimal number

def printOctal(n):
    if(0<=n<=7):
        print(n,end='') 
    else:       
        printOctal(int(n/8))
        print(n%8,end='')

printOctal(int(input("Enter a number to print it's octal: ")))

    