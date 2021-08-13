# from replit import clear
import random

from hangman_art import logo, stages
print(logo)


from words import word_list

chosen_word = random.choice(word_list)

lives = 6


#print(chosen_word)
display = []


no_of_blanks = len(chosen_word)
for blanks in range(no_of_blanks):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = (input("\nguess a letter: ")).lower()

    # clear()

    if guess in display:
        print(f"you've already guessed the letter {guess}.\n")

    for position in range(no_of_blanks):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"you guessed the letter {guess}, that is not in the word. you lose a life.\n")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"you lose. the word was {chosen_word}.")

    print(display)

    if "_" not in display:
        end_of_game = True
        print(f"\n yayy!! you win! you guessed the word {chosen_word} right.")

    print(stages[lives])


