#Write A Script To Enter Any String And Count Vowels
def count_vowels(string):
    n=0
    vowels=['a','e','i','o','u','A','E','I','O','U']
    for i in string:
        if i in vowels:
            n+=1
    print(f"Vowels In String Are {n}")
string=input("\n Enter string ...? :")
count_vowels(string)
