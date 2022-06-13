#import random module
import random

#output the rules of the game 
print('Welcome to the Rock-Paper-Scissors Game \n')
print('The rules of the game include: \n' 
                        + 'Rock wins against Scissors \n'
                        + 'Paper wins against Rock \n'
                        + 'Scissors wins against Paper \n')

while True:
    print('Enter choice \n 1 for Rock, 2 for Paper, 3 for Scissors')

    choice = int(input('Your turn: '))

    while choice >3 or choice <1:

        choice = int(input('Enter valid input: '))

    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    # Print user choice
    print('Your choice is: ' + choice_name)
    print('\n Computer choice........ ')

    comp_choice = random.randint(1,3)

    

    while comp_choice == choice:
        comp_choice = random.randint(1,3)

    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'

    print('Compuer choice is : ' + comp_choice_name)
    print(choice_name + ' versus ' + comp_choice_name)

    if choice == comp_choice:
        print('Draw => ', end = '')
        result = Draw

    #rules for winning
    #'Rock wins against Scissors \n'
    if ((choice == 1 and choice == 3) or (choice == 3 and choice == 1)):
        print('Rock wins =>', end ='')
        result ='Rock'

    #'Paper wins against Rock \n'
    elif ((choice == 1 and choice == 2) or (choice == 2 and choice == 1)):
        print('Paper wins =>', end ='')
        result ='Paper'
    
    #'Scissors wins against Paper \n'
    else: 
        print('Scissors wins =>', end ='')
        result ='Scissors'  

    #Printing whether the computer or the user wins
    if choice == comp_choice:
        print('It is a tie')
    if result == choice:
        print('User Wins')
    else:
        print('Computer Wins')

    print('Do you want to play again? (Y/N)')
    reply = input().lower()

    if reply == 'n':
        break

   
print('\n Thanks for playing our game')