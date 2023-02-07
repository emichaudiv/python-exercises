'The Little Mermaid' == 3
'Brother Bear' == 5
'Hercules' == 1

my_total = (3 + 5 + 1) * 3

print (my_total)
#27

Google = 400 
Amazon =  380 
Facebook = 350 

print ((Facebook * 10) + (Google * 6) + (Amazon * 4))
#7420

class_available = True
class_time = True
free_check = class_available and class_time 
print (free_check)

coupon_check = 2
is_current = True
is_member = False

purchase_w_coupon = (((coupon_check >= 2) and is_current) or is_member)
print (purchase_w_coupon)

cred = dict(username = 'codeup', password = 'notastrongpassword')
p_u_check = (cred ['username'] != cred ['password'])
credential_check = len(cred ['username']) < 20 and len (cred ['password']) >= 5 and p_u_check
print (credential_check)

