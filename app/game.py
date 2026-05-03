import random

def load_words():
    with open("app/words.txt") as f:
        return [w.strip().lower() for w in f.readlines()]

WORDS = load_words()

def get_random_word():
    return random.choice(WORDS)

def check_guess(secret, guess):
    result = []
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            result.append("correct")
        elif guess[i] in secret:
            result.append("present")
        else:
            result.append("absent")
    return result
