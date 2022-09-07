# 4. Write a recursive python function to calculate sum of squares of first N natural
# numbers

def sumSquaresN(n):
    if(n==1):
        return 1
    return n*n+sumSquaresN(n-1)

print("Sum is %d"%sumSquaresN(int(input("Enter a number"))))