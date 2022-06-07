import random

from Day007_hangman_arts import stages, logo
from Day007_hangman_words import word_list

end_of_game = False
lives = len(stages) - 1

print(logo)

chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []

guesses = []

for letter in chosen_word:
    display.append("_")

while not end_of_game:
    guess_letter = input("Guess a letter: ").lower()

    if guess_letter in guesses:
      print("You already guessed " + guess_letter)
    else:
      guesses.append(guess_letter)
      count = 0
      for letter in chosen_word:
          if letter == guess_letter:
              display[count] = letter
          count += 1

      print(f"{' '.join(display)}")

      if guess_letter not in chosen_word:
        print(guess_letter + " is not in the chosen word")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")
            print("Chosen word was: " + chosen_word)

      if "_" not in display:
          end_of_game = True
          print("You win!")

      print(stages[lives])