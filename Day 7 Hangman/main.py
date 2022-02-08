import random
from hangman_words import word_list
from hangman_art import logo,stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
guessed_letters = []


end_of_game = False
lives = 6

print(logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You have already tried the letter: {guess}")
        guessed_letters.append(guess)
        continue
    guessed_letters.append(guess)
    

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"You chose letter: {guess} which is not in the word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])