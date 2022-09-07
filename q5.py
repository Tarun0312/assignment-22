# 5. Write a recursive python function to calculate sum of cubes of first N natural numbers

def sumCubesN(n):
    if(n==1):
        return 1
    return n*n*n+sumCubesN(n-1)

print(sumCubesN(int(input("Enter a number: "))))