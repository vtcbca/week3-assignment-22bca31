#2.Write a python script to enter any number and print the sum of its digit.

def sumofdigit(b):
    a=b
    ram=0
    sum=0
    while(b!=0):
        ram=b%10
        sum=sum+ram
        b//=10
    print(f"The sum of digit of number {a} is {sum}!")  

num=int(input("Enter a number:"))
sumofdigit(num)
