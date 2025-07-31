import random

def play_hangman():
    word_list = ['apple', 'tiger', 'snake', 'plane', 'chair']
    word_to_guess = random.choice(word_list)
    guessed_letters = []
    tries = 6
    hidden_word = ['_'] * len(word_to_guess)

    print("\n🎮 New Game Started!")
    print("Guess the word, one letter at a time.")
    print("You have", tries, "incorrect guesses allowed.\n")

    while tries > 0 and '_' in hidden_word:
        print("Word:", ' '.join(hidden_word))
        print("Guessed Letters:", ', '.join(guessed_letters))
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input. Please enter one letter.\n")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("✅ Good guess!\n")
            for i, letter in enumerate(word_to_guess):
                if letter == guess:
                    hidden_word[i] = guess
        else:
            tries -= 1
            print(f"❌ Wrong guess! You have {tries} tries left.\n")

    # Check win or lose
    if '_' not in hidden_word:
        print("🎉 Congratulations! You guessed the word:", word_to_guess)
        return True  # Win
    else:
        print("💀 Game Over! The word was:", word_to_guess)
        return False  # Loss


# 🎯 Main Game Loop with Scoreboard
wins = 0
losses = 0

while True:
    result = play_hangman()
    if result:
        wins += 1
    else:
        losses += 1

    print(f"\n📊 Scoreboard: Wins = {wins} | Losses = {losses}")
    
    replay = input("🔁 Do you want to play again? (yes/no): ").lower()
    if replay not in ['yes', 'y']:
        print("\n👋 Thanks for playing Hangman!")
        print(f"Final Score: {wins} Wins | {losses} Losses")
        break
