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
