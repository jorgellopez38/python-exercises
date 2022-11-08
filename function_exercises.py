python 

# exercise 1
def is_two(num):
    
    if num == 2 or num == "2":
    
        return True

    else:
        
        return False 
    
is_two("2")   

# 2

def is_vowel(letter):
    
    if letter in ['a', 'e', 'i', 'o', 'u']:
    
        return True
    
    else:
        
        return False
    
is_vowel('a')

# 3

def is_consonant(letter):
    
    if letter not in ['a', 'e', 'i', 'o', 'u']:
    
        return True
    
    else:
        
        return False
    
is_consonant('q')

# 4

def capitalize_if_consonant(word):
    first_letter = word[0]
    if is_consonant(first_letter):
        return word.capitalize()
    else:
        return word

capitalize_if_consonant("bow")

# 5

def calculate_tip(tip, bill):
    calculate_bill = bill * (1 + (tip/100))
    final_amount = "{:.2f}".format(calculate_bill, 2)
    
    if tip == 15:
        print(f"Please pay: ${final_amount}")
    elif tip == 18:
        print(f"Please pay: ${final_amount}")
    else:
        print(f"Please pay: ${final_amount}")
        
# Get inputs
tip = int(input('How much would you like to tip?: 15%, 18%, or 20%? '))
bill = int(input('What was the total bill?: $'))

calculate_tip(tip, bill)
# Thank customer
print('THANK YOU FOR YOUR BUSINESS!!')

# 6

def apply_discount(price, discount):
    discount_amount = price * discount
    return price - discount_amount

apply_discount(50, .15)

# 7

def handle_commas(num):
    return float(num.replace(",", ""))

handle_commas("1,000,000.00")

# 8

def get_letter_grade(letter):
    
    if letter >= 90:
        print('A')
    elif letter >= 80:
        print('B') 
    elif letter >= 70:
        print('C')
    elif letter >= 60:
        print('D')
    else:
        print('F')
        
        

get_letter_grade(87) 

# 9

def remove_vowels(string):
    newstring = []      
    for letter in string:
        if not is_vowel(letter):
            newstring.append(letter)
    return "".join(newstring)


remove_vowels('tread')