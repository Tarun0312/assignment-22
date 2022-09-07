# 10. Write a recursive python function to find the Nth term of the Fibonacci series.

def fibN(n):
    if(n==1):
        return 0
    if(n==2):
        return 1    
    return fibN(n-1)+fibN(n-2)

print("Nth term of fibonacci series is",fibN(int(input("Enter a number: "))))