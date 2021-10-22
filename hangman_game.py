import os
import time
import random

def game_name():
   name = """
▓▓     ▓▓     ▓▓▓     ▓▓▓     ▓▓ ▓▓▓▓▓▓▓▓▓ ▓▓▓    ▓▓▓▓     ▓▓▓     ▓▓▓     ▓▓
▓▓     ▓▓    ▓▓ ▓▓    ▓▓ ▓▓   ▓▓ ▓▓        ▓▓ ▓▓ ▓▓ ▓▓    ▓▓ ▓▓    ▓▓ ▓▓   ▓▓
▓▓▓▓▓▓▓▓▓   ▓▓▓▓▓▓▓   ▓▓  ▓▓  ▓▓ ▓▓▓▓▓▓▓▓▓ ▓▓  ▓▓▓  ▓▓   ▓▓▓▓▓▓▓   ▓▓  ▓▓  ▓▓
▓▓     ▓▓  ▓▓     ▓▓  ▓▓   ▓▓ ▓▓ ▓▓     ▓▓ ▓▓       ▓▓  ▓▓     ▓▓  ▓▓   ▓▓ ▓▓
▓▓     ▓▓ ▓▓       ▓▓ ▓▓    ▓▓▓▓ ▓▓▓▓▓▓▓▓▓ ▓▓       ▓▓ ▓▓       ▓▓ ▓▓    ▓▓▓▓
   """
   print(name)

def creator_name():
   creator = """
------------------------------------------------------------------------------
Created by     :            Fernando Callasaca
Github         :            https://github.com/fernandocallasaca
------------------------------------------------------------------------------
   """
   print(creator)

def hagman_structure():
   hangman = """
|                                        |
|                                        |
|                                        |
|                                        |
|                                        |
|                                        |
|                                        |
|                                        |
|                                        |
|                                        |
|                                        |
|                                        |
|                                        |  
|                                        | 
|                                        |
|                                        |
|                                        |
   """
   # 1 min - max 17 = height
   # 1 min - max 40 = width
   # tuple(width, height, simbol)

   first_line = (
      (17, 7, '_'),
      (17, 8, '_'),
      (17, 9, '_'),
      (17, 10, '_'),
      (17, 11, '_'),
      (17, 12, '_'),
      (17, 13, '_'),
      (17, 14, '_'),
      (17, 15, '_'),
      (17, 16, '_'),
      (17, 17, '_'),
      (17, 18, '_'),
      (17, 19, '_'),
      (17, 20, '_'),
      (17, 21, '_'),
      (17, 22, '_'),
      (17, 23, '_'),
   )

   second_line = (
      (17, 13, '|'),
      (16, 13, '|'),
      (15, 13, '|'),
      (14, 13, '|'),
      (13, 13, '|'),
      (12, 13, '|'),
      (11, 13, '|'),
      (10, 13, '|'),
      (9, 13, '|'),
      (8, 13, '|'),
      (7, 13, '|'),
      (6, 13, '|'),
      (5, 13, '|'),
      (4, 13, '|'),
   )

   third_line = (
      (3, 13, '_'),
      (3, 14, '_'),
      (3, 15, '_'),
      (3, 16, '_'),
      (3, 17, '_'),
      (3, 18, '_'),
      (3, 19, '_'),
      (3, 20, '_'),
      (3, 21, '_'),
      (3, 22, '_'),
      (3, 23, '_'),
      (3, 24, '_'),
      (3, 25, '_'),
      (3, 26, '_'),
   )

   four_line = (
      (7, 13, '/'),
      (6, 14, '/'),
      (5, 15, '/'),
      (4, 16, '/'),
   )

   fifth_line = (
      (4, 27, '|'),
      (5, 27, '|'),
   )

   sixth_line = (
      (6, 25, '-'),
      (6, 26, '-'),
      (6, 27, '-'),
      (6, 28, '-'),
      (6, 29, '-'),
      (7, 24, '/'),
      (7, 30, '\\'),
      (8, 24, '\\'),
      (8, 30, '/'),
      (8, 25, '_'),
      (8, 26, '_'),
      (8, 27, '_'),
      (8, 28, '_'),
      (8, 29, '_'),
      (7, 26, '*'),
      (7, 28, '*'),
      (7, 27, '.'),
      (8, 27, '~'),
   )

   seventh_line = (
      (9, 27, '|'),
      (10, 27, '|'),
      (11, 27, '|'),
      (12, 27, '|'),
      (13, 27, '|'),
      (14, 27, '|'),
      (15, 27, '|'),
   )

   eight_line = (
      (11, 28, '/'),
      (10, 29, '/'),
   )

   nineth_line = (
      (11, 26, '\\'),
      (10, 25, '\\'),
   )

   tenth_line = (
      (16, 28, '\\'),
      (17, 29, '\\'),
   )

   eleventh_line = (
      (16, 26, '/'),
      (17, 25, '/'),
   )

   part_scene = []

   part_scene += first_line
   part_scene += second_line
   part_scene += third_line
   part_scene += four_line
   part_scene += fifth_line
   part_scene += sixth_line
   part_scene += seventh_line
   part_scene += eight_line
   part_scene += nineth_line
   part_scene += tenth_line
   part_scene += eleventh_line

   lines = [list(line) for line in hangman.splitlines()]

   for part_man in part_scene:
      lines[part_man[0]][part_man[1]] = part_man[2]

   scene = '\n'.join([''.join(l) for l in lines])
   print(scene)

def list_words():
   my_list_words = []
   with open('./files/data.txt', 'r', encoding='utf-8') as file:
      my_list_words = [word[:len(word) - 1] for word in file]
   return my_list_words

def check_word(correct_word, current_word, letter):
   string = ''
   for i, let in enumerate(correct_word):
      if let.lower() == letter.lower():
         current_word[i] = letter
         string += letter.lower() + ' '
      else:
         if(current_word[i] != '_'):
            string += current_word[i].lower() + ' '
         else:
            string += '_ '
   print('Word:', string)
   return '_' in current_word

def generate_scene(correct_word, current_word, letter):
   # Clean the window
   os.system('cls')
   # Game Name
   game_name()
   # Creator name
   creator_name()
   # Hagman Structure for each game defeat
   hagman_structure()
   # Check word and return if is complete or not
   return check_word(correct_word, current_word, letter)

def run():
   my_list_words = list_words()
   correct_word = random.choice(my_list_words)
   current_word = ['_' for i in correct_word]
   generate_scene(correct_word, current_word, '$5=&')

   alive = True
   incomplete = True
   
   while (alive == True and incomplete):
      # we need a letter
      letter = str(input('Type a letter: '))
      # incomplete = check_word(correct_word, current_word, letter)
      incomplete = generate_scene(correct_word, current_word, letter)

if __name__ == '__main__':
   run()