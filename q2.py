# 2. Write a recursive python function to calculate sum of first N odd natural numbers

def sumNOdd(n):
    if(n==1):
        return 1
    return 2*n-1+sumNOdd(n-1)
print("Sum is %d"%(sumNOdd(int(input("Enter a number: "))))  )  