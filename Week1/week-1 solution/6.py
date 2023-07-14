#6.Write a python script to enter any string and print only part of string. Take input of start character and end character from user.

def partstr(stri):
    st=int(input("Enter start position:"))
    en=int(input("Enter end position:"))
    part=stri[st-1:en:]    
    print(f"The part of the string '{stri}' is '{part}'")


string=input("Enter a string:")
partstr(string)
