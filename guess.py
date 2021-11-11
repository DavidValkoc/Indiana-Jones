#!/usr/bin/env python3
import random


def play_game(secret=7):
   print("Myslím si číslo od '1' do '20'.")
   tip = None
   counter = 5

   while counter > 0 and secret != tip:
       tip = input('Tvoj tip: ')
       tip = int(tip)

       if secret > tip:
           print(f'Hmm... Moje číslo je väčšie ako {tip}.')
           counter = counter - 1

       elif secret < tip:
           print(f'Hmm... Moje číslo je menšie ako {tip}.')
           counter = counter - 1

       else:
           print('Ta ty si genius!')

   if counter == 0:
       print('Game over.')


if __name__ == '__main__':
   repeat = 'ano'

   while repeat == 'ano':
       play_game(random.randint(1, 20))
       repeat = input('Chceš si zahrať znova? (ano/nie) ').lstrip().rstrip().lower()

   print('Ďakujem za hru SI FRAJER !!!!!!.')
