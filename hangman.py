import random
import subprocess
import os
from hangmanlogo import logo,steps
from hangman_words import words
from time import sleep

lives = 0

print(logo)

chosen_word = random.choice(words).lower()


length_word = len(chosen_word)

#puting in a list blank spaces as length of chosen word
display = []
for _ in range(length_word):
  display+="_"
print(f"{' ' .join(display)}")


end_of_game=False

while  not end_of_game:
 guess = input("\n Guess the letter: ").lower()
 sleep(1)
 os.system('cls')
 if guess in display:
  print(f"You've already guessed {guess}")
#check guess letter
 for position in range(length_word):
  letter=chosen_word[position]
  if letter==guess:
   display[position]=letter


 if guess not in chosen_word:
  print(f"You guessed {guess}, that's not in the word. You lose a life") 
  lives+=1
  if lives==6:
    end_of_game=True
    print("\nyou lose")

 print(f"{' '.join(display)}")

 if "_" not in display:
  end_of_game=True  
  print("\nYou Win")

 print(steps[lives])




    
    


