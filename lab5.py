'''
lab5
'''

#3.1

alien_color = 'green'

if alien_color == 'green':
    print('you have earned 5 points')
    
#3.2

alien_color = 'red'

if alien_color == 'green':
    print('you have earned 5 points')
    
else:
        print('you have earned 10 points')
        
#3.3

favorite_fruits=['apple','banana','orange']

if 'banana' in favorite_fruits:
    print('you really like banana')
  
if 'apple' in favorite_fruits:
    print('you really like apple')
    
if 'orange' in favorite_fruits:
    print('you really like orange')
    
#3.4

age = 75

if age <10:
    print('kid')
    
elif age >=10 and age<20:
    print('teenager')
    
else:
    print('adult')
    
if age>= 65:
    print('elder')