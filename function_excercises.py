def is_two(n):
    if (n == 2) or (n == '2'):
       return True
    else :
        return False
two = is_two(2)
print(two)

def is_vowel(v):
    if v == 'a' or \
    v == 'e' or \
    v == 'i' or \
    v == 'o' or \
    v == 'u':
        return True
    else:
        return False
letter_u = is_vowel('u')
print(letter_u) 

def is_consonant(c):
    if c in['a','e','i','o','u'] :
        return False
    else:
        return True
letter_b = is_consonant('b')
print(letter_b) 

def big_consonant(d):
    if  d in['a','e','i','o','u']:
        return 'That is a vowel, not a consanant!'
    else:
        return d.capitalize()
letter_g = big_consonant('great')
print(letter_g)

payment = 15.00

def calculate_tip(t):
    return float(t) * float(payment) 
fifteen_percent =calculate_tip(.15)
print(fifteen_percent)

def apply_discount(m):
    return payment - (float(m) * float(payment)) 
fifty_off = apply_discount(.50)
print(fifty_off)

def handle_commas(h):
    if ',' in h:
        number = h.replace(',','')
        return int(number)
comma_off = handle_commas('1,000')
print(comma_off)

def get_letter_grade(l):
    if l >= 93:
        return 'A'
    elif l >= 80:
        return 'B'
    elif l >= 70:
        return 'C'
    elif l >= 60:
        return 'D'
    else:
        return 'F'
just_okay = get_letter_grade(75)
print(just_okay)

def remove_vowels(v):
    letter = v.replace('a','').replace('e','').replace('i','').replace('o','').replace('u','')
    return letter
salad = remove_vowels('The quick brown fox jumped over the lazy dog.')
print(salad)

def normalize_name(n):
    n = n.strip().lower()
    n = n.replace('_','  ')
    nn = ''
    for let in n:
        if not let.isdigit() or not let.isalpha():
            nn += let
    return nn

baby_input = normalize_name('o7tvngfafniwmrgaoltgvar7o48')
print(baby_input)

# def cumulative_sum(s):
#     count = 0
#     list = 0
#     for s in list:
#         count += s
#         list.append(count)
#     return list
# math_stuff = cumulative_sum([1,3,5])
# print(math_stuff)