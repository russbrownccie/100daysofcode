import random
import hangman_words
from hangman_art import logo
from hangman_art import stages

print(logo)

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6




display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
      print(f"You already chose {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:

        lives -= 1
        print (f"{guess} is not in the word")
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was {chosen_word}")

    print(f"{' '.join(display)}")


    if "_" not in display:
        end_of_game = True
        print("You win.")



    print(stages[lives])
