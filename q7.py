# 7. Write a recursive python function to calculate sum of the digits of a given number

def sumDigits(n):
    if(n==0):
        return 0
    return n%10+sumDigits(int(n/10))

print("Sum of digits of a given number=",sumDigits(int(input("Enter a number: "))))