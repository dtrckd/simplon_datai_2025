import random

num = random.randint(1, 1000)
  

while num > 0:
    user_input = int(input('Enter Number: '))

    if user_input < num:
        print('Ton num est trop petit essaie encore mon petit poulet!')
        continue
    elif user_input > num:
        print('Ton num est trop grand essaie encore mon petit poulet!')
        continue
    else: 
        user_input == num
        print ('tu as gagné ma pucinette!')
        break
        
        
        
        
        