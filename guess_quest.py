import random

class WordGame:
    def __init__(self, word_bank):
        self.word_bank = word_bank
        self.word_to_guess = random.choice(word_bank)
        self.misplaced_letters = set()
        self.incorrect_letters = set()

    def check_guess(self, guess):
        result = ""
        for i in range(len(guess)):
            if guess[i] == self.word_to_guess[i]:
               result += guess[i]
            elif guess[i] in self.word_to_guess:
                 result += "_"
                 self.misplaced_letters.add(guess[i])
            else:
                result += "_"
                self.incorrect_letters.add(guess[i])
        return result


    def current_state_display(self):
        print("Misplaced letters:", self.misplaced_letters)
        print("Incorrect letters:", self.incorrect_letters )

class GameManager:
    def __init__(self, max_turns=5):
        self.max_turns = max_turns
        self.turns_taken = 0
        self.word_bank = ["queen", "helps", "learn", "flash", "blaze"]
        try:
            self.game = WordGame(self.word_bank)
        except Exception as e:
            print(f"Error starting game: {e}")
            exit()


    def display_intro(self):
        print("\nWelcome to Guess Quest!")
        print(f"The word has {len(self.game.word_to_guess)} letters.")
        print(f"You have {self.max_turns} turns to guess the word.\n")

    def play_turn(self):
        try:
           guess = input("Guess the word: ").lower()

           if len(guess) != len(self.game.word_to_guess):
            print(f"Error: Too long! Please enter a {len(self.game.word_to_guess)}-letter word")
            return False

           self.turns_taken += 1

           if guess == self.game.word_to_guess:
            print("Congratulations, you win!")
            return True

           result = self.game.check_guess(guess)
           print(f"Result: {result}")
           self.game.current_state_display()
           return False

        except Exception as e:
            print(f"Error during game: {e}")
            return True

    def play(self):
        self.display_intro()

        while self.turns_taken < self.max_turns:
            if self.play_turn():
                return
            print(f"You have {self.max_turns - self.turns_taken} turns left.\n")

        print(f"\nGame Over! The word was '{self.game.word_to_guess}'")


game = GameManager()
game.play()


