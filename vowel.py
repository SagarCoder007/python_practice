str1 = input("enter string :")
vowel = "aeiocAEIOU"
vow=0
cons=0
for i in str1:
        if i in vowel:
            vow+=1
        else:
            cons+=1

print(f"no of vowels are {vow} and consonant are {cons}")