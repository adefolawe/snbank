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

                while True:  
                    acct_name= input('Account Name: ').capitalize()
                    if not all(x.isalpha or x == "" for x in acct_name):
                        print("Your name must consist of letters only.")
                        continue
                    else:
                        break
                
                while True:
                    print("Type of account: Savings or Current?")
                    acct_type= input("Account Type: ").capitalize()
                    if not acct_type.isalpha():
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
                    email_add = input('Email Address: ').lower()
                    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email_add)
                    if match == None:
                        print('Invalid email address')
                        continue
                    else:
                        break
                while True:
                    acct_num_list = [random.randint(0, 9) for _ in range(10)]
                    acct_num = ''.join(map(str, acct_num_list))
                    print(f"The Customer {acct_name} has the Account Number {acct_num}")
                    break


                with open(f'customers.txt', 'a+') as f:
                    for details in [acct_name, opening_bal, acct_type, email_add, acct_num]:
                        f.write(f'{details}, ')
                    f.write('\n')
                
            elif staff_operations_input == "2":
                print("enter your account number")
                check_acct_num = input('Enter Account Number: ')
                with open('customers.txt') as file:
                    for line in file:
                        acct_name, opening_bal, acct_type, email_add, acct_num = line[:-3].split(',')
                        if check_acct_num == acct_num.strip(' '):
                            print(f'Account Name : {acct_name} \nOpening Balance : {opening_bal} \nAccount Type : {acct_type} \nEmail Address : {email_add} \nAccount Number : {acct_num}')
                    
            elif staff_operations_input == "3":
                print("You have logged out")
                break
            
        else:
            print("Invalid login information, try again")
             
      
       
while staff_login_input == "2":
    print("Goodbye")

while staff_login_input != "1" or "2":
    input("Please choose '1' to login or '2' to close the app: ")
