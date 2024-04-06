import secrets
import string
# define the Code_Ascii
numbers=string.digits
special_characters=string.punctuation
capital_letters=string.ascii_uppercase
lowercase=string.ascii_lowercase
Code_Ascii=lowercase+capital_letters+numbers+special_characters
#CONDITIONS
print("A strong password must contain:")
print("-At least one number.")
print("-At least one symbol.")
print("-At least one uppercase and lowercase letter.")
print("Therefore, its minimum length must be 4. TAKE THIS INTO CONSIDERATION.")
print()
#Validation
while True:
    #password length:
    length=input("Enter your password length: ")
    if all(x in numbers for x in length):
        length=int(length)
        if length>3:
            break
        else:
           print("You did not enter a valid length, please try again.") 
    else:
        print("You did not enter a valid length, please try again.")

# creating the password:
while True:
    password=""
    for i in range(length):
        password+="".join(secrets.choice(Code_Ascii))
    if (any(x in special_characters for x in password) and any(x in numbers for x in password) and 
        any(x in capital_letters for x in password) and any(x in lowercase for x in password)):
        break

print(password)