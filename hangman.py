import random

def ch_word():
    words = ["python", "hangman", "programming", "computer", "code", "developer", "challenge"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman(guess,word_to_guess,guessed_letters):
    incorrect_attempts = 0
    max_attempts = 5

    while True:
        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You've already guessed that letter. Try again.")
            elif guess in word_to_guess:
                print("Good guess!")
                guessed_letters.append(guess)
            else:
                print("Incorrect guess.")
                incorrect_attempts += 1
                guessed_letters.append(guess)

            if incorrect_attempts == max_attempts:
                print("Sorry, you've run out of attempts. The word was:", word_to_guess)
                break
            elif set(word_to_guess) <= set(guessed_letters):
                print("Congratulations! You've guessed the word:", word_to_guess)
                break
if __name__ == "__main__":
    hangman()
