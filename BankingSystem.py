import random
import string
import re
#import numpy as np

#i = np.range(10)


print("=====================================")
print(" ----Welcome to SN Bank----       ")
print("*************************************")
print("=<< 1. Staff Login                >>=")
print("=<< 2. Close App                  >>=")
print("*************************************")

file = open("staff.txt")
staff_details = file.read().strip().split()

staff_login_input = input("Select your choice number from the above menu : ")

if staff_login_input == "1":
    
        print("Enter your login details")
        userName = input('username: ').lower()
        password = input('password: ').lower()
        
        while userName and password in staff_details:
            print(" ")
            print("*************************************")
            print("=<< 1. Create new bank account    >>=")
            print("=<< 2. Check Account Details      >>=")
            print("=<< 3. Logout                     >>=")
            print("*************************************")
            staff_operations_input = input("Select your choice number from the above menu : ")

            if staff_operations_input == "1":
                file=open("customers.txt",'a+')

                while True:  
                    first_n= input('First Name: ').capitalize()
                    if not first_n.isalpha():
                        print("Your name must consist of letters only.")
                        continue
                    else:
                        break
                while True: 
                    last_n= input('Last Name: ').capitalize()
                    if not last_n.isalpha():
                        print("Your name must consist of letters only.")
                        continue
                    else:
                        break
                while True:
                    acct_type= input("Savings or Current Account?: ").capitalize()
                    if not last_n.isalpha():
                        print("Your account type can only consist of letters only.")
                        continue
                    else:
                        break

                while True:
                    opening_bal = input("Opening Balance: ")
                    match = re.match('^[0-9]', opening_bal)
                    if match == None:
                        print('Invalid opening balance. Please input numbers only')
                        continue
                    else:
                        break                
                   
                while True:
                    email_add = input('Email Adress: ').lower()
                    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email_add)
                    if match == None:
                        print('Invalid email address')
                        continue
                    else:
                        break


                details_list = first_n, last_n, acct_type, opening_bal, email_add, ''
                for items in details_list:
                    file.write(items+"\n")
                print(details_list)
                
            elif staff_operations_input == "2":
                print("enter your account number")
                file = open("customers.txt")
                customers = file.read().strip().split()
                acct_num = input("Account Number: ")
                if opening_bal in customers:
                    print(f"{first_n} {last_n} {acct_type} {opening_bal} {email_add}")
                    
            elif staff_operations_input == "3":
                    close()

        if userName and password not in staff_details:
            print("Invalid login information, try again")

               
      
       
if staff_login_input == "2":
    print("Goodbye")

else:
    input("Wrong entry. Please choose '1' to login or '2' to close the app: ")
