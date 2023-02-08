Monday_yes = input('Is today Monday?')

if Monday_yes == "Yes" or Monday_yes == "yes": 
        print ("Liar")
elif Monday_yes == "No" or Monday_yes == "no":
        print ("Thank you")
        Weekend_check = input('Is it the weekend?')
        if Weekend_check == "Yes" or Weekend_check == "yes": 
            print ("Awesome!")
        elif Weekend_check == "No" or Weekend_check == "no":
            print ("okay...")
else:
      print ("Wrong input")
      
extra_hours = 0
paycheck_hour = input('How many hours worked this week?')
paycheck_rate = input('What is the employee\'s hourly rate?')
if int(paycheck_hour) > 40 :
    extra_hours = (int(paycheck_hour) - 40) + int(extra_hours)
print (int(paycheck_hour) * int(paycheck_rate) + ((int(extra_hours)* int(paycheck_rate))*1.5))

i = 5
while i <= 15:
      print (i)
      i += 1

e = 0
while e <= 98:
      print (e)
      e += 2
while e >=-10:
      print(e)
      e -= 5

b = 2
while b <= 1000000:
      print (b)
      b = b*b

h = 100
while h >= 0:
      print(h)
      h -= 5

m = input('Pick a number, and it shall be multiplied, 1 through 10!:') 
if int(m) != int(m):
      print ('Numbers only!')
answer = 0
print(m + ' x 1 = ' + str(int(m)*1))
print(m + ' x 2 = ' + str((int(m) * 2)))
print(m + ' x 3 = ' + str((int(m) * 3)))
print(m + ' x 4 = ' + str((int(m) * 4)))
print(m + ' x 5 = ' + str((int(m) * 5)))
print(m + ' x 6 = ' + str((int(m) * 6)))
print(m + ' x 7 = ' + str((int(m) * 7)))
print(m + ' x 8 = ' + str((int(m) * 8)))
print(m + ' x 9 = ' + str((int(m) * 9)))
print(m + ' x 10 = ' + str((int(m) * 10)))

intergers = [1,2,3,4,5,6,7,8,9]
for i in intergers:
    print((str(i) * int(i))) 

pos_please = input('Give me a even number.')
while int(pos_please) != 0 :
    if pos_please.isdigit() :
        if int(pos_please)%2 == 0:
            print('Fine job!')
            break
        elif int(pos_please)%2 != 0:
                pos_please = input('A EVEN number please.')
        else :
                pos_please = input('ONlY a number please.')


while True:
      my_num = input('Please enter interger: \n')
      if my_num.isdigit():
            my_num = int(my_num)
            print('number | square | cube|')
            print('------------------------')
            for i in range(1,my_num+1):
                print(f'{i:^7}| {i**2:^7}| {i**3:^6}')
            continue_var = input('Enter more intergers?')
            if continue_var.lower().startswith('n'):
                  break