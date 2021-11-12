import random
import os
import time

def clear_screen():
    os.system('cls')

def print_rock():
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)

def print_paper():
    print("""
         _______
    ---'    ____)____
                ______)
               _______)
              _______)
    ---.__________)
    """)

def print_scissors():
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

def game_screen():

    while True:

        clear_screen()

        print('\nCo wybierasz?')
        print('\n\t1 - PAPIER')
        print('\t2 - KAMIEŃ')
        print('\t3 - NOŻYCE')
        print('\n\t0 - Wyjście')

        computer_choice = random.choice(['PAPIER', 'KAMIEŃ', 'NOŻYCE'])
        try:
            user_choice = int(input('\nWybieram: '))

            if user_choice == 1 and computer_choice == 'PAPIER':
                print_paper()
                print(f'\n\n\t\tKomputer wybrał {computer_choice}, REMIS!')
            elif user_choice == 1 and computer_choice == 'KAMIEŃ':
                print_rock()
                print(f'\n\n\t\tKomputer wybrał {computer_choice}, WYGRAŁEŚ!')
            elif user_choice == 1 and computer_choice == 'NOŻYCE':
                print_scissors()
                print(f'\n\n\t\tKomputer wybrał {computer_choice}, PRZEGRAŁEŚ!')
            elif user_choice == 2 and computer_choice == 'PAPIER':
                print_paper()
                print(f'\n\n\t\tKomputer wybrał {computer_choice}, PRZEGRAŁEŚ!')
            elif user_choice == 2 and computer_choice == 'KAMIEŃ':
                print_rock()
                print(f'\n\n\t\tKomputer wybrał {computer_choice}, REMIS!')
            elif user_choice == 2 and computer_choice == 'NOŻYCE':
                print_scissors()
                print(f'\n\n\t\tKomputer wybrał {computer_choice}, WYGRAŁEŚ!')
            elif user_choice == 3 and computer_choice == 'PAPIER':
                print_paper()
                print(f'\n\n\t\tKomputer wybrał {computer_choice}, WYGRAŁEŚ!')
            elif user_choice == 3 and computer_choice == 'KAMIEŃ':
                print_rock()
                print(f'\n\n\t\tKomputer wybrał {computer_choice}, PRZEGRAŁEŚ!')
            elif user_choice == 3 and computer_choice == 'NOŻYCE':
                print_scissors()
                print(f'\n\n\t\tKomputer wybrał {computer_choice}, REMIS!')
            elif user_choice == 0:
                clear_screen()
                print('\t\t\nDO ZOBACZENIA!\n\n')
                quit()
            else:
                print('\n\tBłędny wybór, powtórz...')
                time.sleep(2)
                continue

            print()
        
        except ValueError:
            print('\n\tBłędny wybór, powtórz...')
            time.sleep(2)
            continue

        time.sleep(3)

game_screen()