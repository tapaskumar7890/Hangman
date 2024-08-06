import random

# Word categories
word_categories = {
    "Animals": ["elephant", "giraffe", "kangaroo", "dolphin", "crocodile"],
    "Countries": ["argentina", "belgium", "canada", "denmark", "egypt"],
    "Movies": ["inception", "gladiator", "titanic", "avatar", "matrix"]
}

# Hangman graphics
hangman_graphics = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

def choose_category():
    print("Choose a category:")
    categories = list(word_categories.keys())
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")
    choice = int(input("Enter the number of the category: ")) - 1
    return categories[choice]

def get_word(category):
    return random.choice(word_categories[category]).upper()

def display_hangman(tries):
    print(hangman_graphics[tries])

def play_game():
    print("Welcome to Hangman!")
    category = choose_category()
    word = get_word(category)
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 0
    max_tries = 6

    print(f"Category: {category}")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries < max_tries:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the letter {guess}")
            elif guess not in word:
                print(f"{guess} is not in the word.")
                tries += 1
                guessed_letters.append(guess)
            else:
                print(f"Good job! {guess} is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed the word {guess}")
            elif guess != word:
                print(f"{guess} is not the word.")
                tries += 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Invalid guess.")

        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("Congratulations! You guessed the word!")
    else:
        print(f"Sorry, you ran out of tries. The word was {word}. Better luck next time!")

def main():
    play_game()
    while input("Play Again? (Y/N) ").upper() == "Y":
        play_game()

if __name__ == "__main__":
    main()
