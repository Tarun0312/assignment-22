# 3. Write a recursive python function to calculate sum of first N even natural numbers

def sumNEven(n):
    if(n==1):
        return 2*n
    return 2*n+sumNEven(n-1)

print("Sum is {}".format(sumNEven(int(input("Enter a number: ")))))