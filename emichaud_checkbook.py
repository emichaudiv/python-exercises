import sys
import os
import time
local_time = time.ctime()
with open('fake_cred.txt') as f:
    contents = f.readlines()
with open('fake_cred_time.txt') as t:
    time_log = str(t.readlines())

intro = ('Greetings, \nToday\'s exact date is: \n' + local_time + '\nPlease select a number to begin. \n 1.View Balance \n 2.Add Debit (Withdrawl) \n 3.Add credit (Deposit) \n 4.Recent Transaction \n 5.Exit')
print()
print(intro)

def bal_check():
    return contents[0]

def add_debit():
    debit_check = input("Enter:")
    while debit_check.isdigit() != True:
        debit_check = (input("Please Enter Digits:"))
    debit_str = int(contents[0])-int(debit_check)
    debit_tra = str(debit_str)
    with open("fake_cred.txt", "w") as f:
        f.write(debit_tra)
    return 

def add_credit():
    credit_check = input("Enter:")
    while credit_check.isdigit() != True:
        credit_check = (input("Please Enter Digits:"))
    credit_str = int(contents[0])+int(credit_check)
    credit_tra = str(credit_str)
    with open("fake_cred.txt", "w") as f:
        f.write(credit_tra)
    return 


while True:
    local_time = time.ctime()
    with open('fake_cred_time.txt') as f:
        for line in f:
            pass
    last_line = line
    num = input('Awaiting input:')
    while num.isdigit() != True:
        num = input('Please enter 1-5:')
    num_input = int(num)
    if num_input != 1 and num_input != 2 and num_input != 3 and num_input != 4 and num_input != 5:
        continue
    if num_input == 5:
        print('GoodBye.')
        break
    else:
        with open('fake_cred_time.txt') as f:
            for line in f:
                pass
        num_input = int(num)
    if num_input == 1:
        print('Checking Balance:')
        bal_total = bal_check()
        print("$ " + bal_total)
    if num_input == 2:
        print('Enter Debit Amount')
        debit_input = add_debit()
        print("Transaction Successful")
        with open('fake_cred.txt') as f:
            contents = f.readlines()
        with open('fake_cred_time.txt','a') as t:
            t.write('\n' + local_time)
        print (contents)
    if num_input == 3:
        print('Enter Credit Amount')
        credit_input = add_credit()
        print("Transaction Successful")
        with open('fake_cred.txt') as f:
            contents = f.readlines()
        with open('fake_cred_time.txt','a') as t:
            t.write('\n' + local_time)
        print (contents)
    if num_input == 4:
        print ('Your most recent transaction was ' + last_line)
    
print('Thank you, Have a nice day!')