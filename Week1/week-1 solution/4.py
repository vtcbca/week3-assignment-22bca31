#4.Write a python script to enter any number, if it is integer number, then check its armstrong or not. Print appropriate message if it is not palindrom.

def arms(n):
    if(n.isdigit()):
   
        n=int(n)
        ans=n
        rem=0
        sum=0
   
        while(n!=0):
            rem=n%10
            sum=sum+(rem**3)
            n=n//10
        if(ans==sum):
            print(f"The number {ans} is an armstrong number!")
        else:
            print(f"The number {ans} is  not an armstrong number!")
    else:
        print(f"The given input {n} is not valid number!!")


number=input("Enter a number!!:")
arms(number)
