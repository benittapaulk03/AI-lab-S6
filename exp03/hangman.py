import random

def select_random_word():
    words = ["apple", "banana", "orange", "grape", "watermelon"]
    return random.choice(words)

def print_hangman(attempts):
    hangman_figures = [
        
        """
           ________
          |        
          |        
          |       
          |        
          |       
        __|__
        """,
        """
           ________
          |        
          |        O
          |       
          |       
          |
        __|__
        """,
        """
           ________
          |        |
          |        O
          |       
          |
          |
        __|__
        """,
        """
           ________
          |        |
          |        O
          |       /|
          |
          |
        __|__
        """,
        """
           ________
          |        |
          |        O
          |       /|\\
          |
          |
        __|__
        """,
        """
           ________
          |        |
          |        O
          |       /|\\
          |       / 
          |
        __|__
        """,
        """
           ________
          |        |
          |        O
          |       /|\\
          |       / \\
          |
        __|__
        """
    ]
    
    print(hangman_figures[attempts])


def guess_word(word):
    max_attempts = 6
    guessed_word = ['_'] * len(word)
    attempts = 0
    
    print("Welcome to the Word Guessing Game!")
    print("Try to guess the characters in the word.")
    print("You have", max_attempts, "attempts.")
    print("The word contains", len(word), "characters.")
    
    while attempts < max_attempts and '_' in guessed_word:
        print("\nWord:", " ".join(guessed_word))
        guess = input("Enter a character: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
            continue
        
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
            print("Correct guess!")
        else:
            print("Incorrect guess!")
            attempts += 1
            print_hangman(attempts)
    
    if '_' not in guessed_word:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nSorry, you ran out of attempts. The word was:", word)

def main():
    name = input("Enter your name: ")
    word = select_random_word()
    print("Hello,", name + "! Let's play a word guessing game.")
    guess_word(word)

if __name__ == "__main__":
    main()
