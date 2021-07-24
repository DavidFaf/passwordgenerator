from flask import Flask
import random


lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = lower_case.upper()
numbers = "0123456789"
symbols = "[]{}()*:/,._-"

print("This program generates a secure password\n----------------------\n")

def secure_password():
            secure = lower_case + upper_case + numbers + symbols
            length = int(input("How long do you want your password to be (How many characters): "))
            password = "".join(random.sample(secure, length))
            print(f"Your randomly generated password is: {password}")
            return password

rand_p = secure_password()
save_passpword = input("Do you want to save your password? (y/n) \n---------")

if save_passpword.lower() == "y":
    def save_to_file(path):
            with open(f"{path}", 'w') as file:
                file.write(rand_p)
                print(f"Your password has been saved to \'{path}\' :) ")

    try:
        save_to_file(r'C:\Users\HP\Desktop\Haq\New folder\bots\Random_password_generator\password.txt')
    except:
        print("An error occured, your password couldn't be saved")
    finally:
        print("-------------")

elif save_passpword.lower() == "n":
    print("Alright then")

else:
    print("Incorrect input, please check your input")




