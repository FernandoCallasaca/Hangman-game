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
      (17, 7, '-'),
      (17, 8, '-'),
      (17, 9, '-'),
      (17, 10, '-'),
      (17, 11, '-'),
      (17, 12, '-'),
      (17, 13, '-'),
      (17, 14, '-'),
      (17, 15, '-'),
      (17, 16, '-'),
      (17, 17, '-'),
      (17, 18, '-'),
      (17, 19, '-'),
      (17, 20, '-'),
      (17, 21, '-'),
      (17, 22, '-'),
      (17, 23, '-'),
   )

   second_line = (
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
   )

   third_line = (
      (4, 13, '-'),
      (4, 14, '-'),
      (4, 15, '-'),
      (4, 16, '-'),
      (4, 17, '-'),
      (4, 18, '-'),
      (4, 19, '-'),
      (4, 20, '-'),
      (4, 21, '-'),
      (4, 22, '-'),
   )

   four_line = (

   )

   scene_descriptors = []

   # if self.strikes >= 1:
   scene_descriptors += first_line
   scene_descriptors += second_line
   scene_descriptors += third_line
   scene_descriptors += four_line


   lines = [list(line) for line in hangman.splitlines()]

   for descriptor in scene_descriptors:
      lines[descriptor[0]][descriptor[1]] = descriptor[2]

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