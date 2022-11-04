
#control_structures_exercises

# 1a
day_of_week = True

if day_of_week:
    print('Today is not Monday')
else:
    print('Today is Monday')
    
# 1b  
day_of_week = True

if day_of_week:
    print('Today the weekend')
else:
    print('Today is not the weekend')

 # 1c   
hours_worked_in_a_week = 45
hourly_rate = 50 
weekly_paycheck = 3600
overtime = 1.5

if hours_worked_in_a_week > 40:
    print((hours_worked_in_a_week * hourly_rate) * overtime)

# 2
i = 5
while i <= 15:
    print (i)
    i += 1
i = 2


while i <= 100:
    print (i)    
    if i == 100: 
        break
    i += 2
i = 100


while i >= -10:
    print (i)    
    if i == -10: 
        break
    i -= 5
i = 2


while i < 1_000000:
    print(i)
    if i > 1_000000:
        break
    i = i ** 2
i = 100


while i >= 5:
    
    print (i)       
    if i < 5:      
        break        
    i -= 5
    
    
number = 7
for i in range(1, 11):
    print(number, 'x', i, '=', number*i)
    
    rows = int(input(10))


for i in range(10):
    for j in range(i+1):
        print(j+1, end= " ")
    print ("\n)")
    
i = 20
while i > 0:
    print (i)
    if i == 1:
        break
    i -= 1
    
x = input("18")
while i < 21:
    print (x)
    if i == 20:
        break
    i += 1
    

odd_numbers_count = 1
for i in range(50):
    if i % 2 == 1:   
        if i == 48:
            print(i)
            continue
        else:
            print("Yikes! Skipping number: 48")
    odd_numbers_count += 1
odd_numbers_count
# 3
for i in range(1,101):
    if i % 15 == 0: 
        print(str(i) + ' FizzBuzz')
    elif i % 3 == 0:
        print(str(i) + ' Fizz')
    elif i % 5 == 0:
        print(str(i) + ' Buzz')
    else:
        print(str(i))
# 4
# 4

your_num = int(input('Input your number here: '))
counter = 1
print('number | squared | cubed')
print('----- | ----- | -----')
while counter <= your_num:
    print(f'{counter}    |)
counter += 1

# 5 

while True:
    your_num = int(input('Input your grade here: '))
    if your_num >= 88:
        print('A')
    elif your_num >= 80:
        print('B') 
    elif your_num >= 67:
        print('C')
    elif your_num > 60:
        print('D')
    else:
        print('F')
    your_input = input('Do you want to continue? Y/N ')
    if your_input_lower().strip() == 'n':
        break

books_read = [{'title': 'The scary blah', 'author': 'Mr Blah', 'genre': 'horror'},        
              {'title': 'The love blah', 'author': 'Mr Love', 'genre': 'romance'},
              {'title': 'The alien blah', 'author': 'Mr Alien', 'genre': 'scify'}]
          
for book in books_read:
    print('Title: {}.'.format(book['title']))   
    print('Author: {}.'.format(book['author']))   
    print('Genre: {}.'.format(book['genre']))  
print()