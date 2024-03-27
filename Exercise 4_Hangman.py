import random

#List secret words
secret_words = ["hangman", "python", "coding", "program", "script"]
used_words = []
global score
score = {'win': 0, 'lose': 0}

def main():
    global score
    while True:
        if len(used_words) == len(secret_words):
            print("You've played with all the words we have!")
            break
        
        #Pilih random secret word yang belum dipakai sebelumnya
        secret = random.choice([word for word in secret_words if word not in used_words])
        used_words.append(secret)
        
        guess = "_ " * len(secret)
        correct = []
        wrong_guesses = 0
        guessed_letters = []
        
        while True:
            print("Guess this: ", guess)
            letter = input("Guess a letter: ").lower()
            
            if letter in guessed_letters:
                print("You have already guessed that letter. Try a different letter!")
                continue
            else:
                guessed_letters.append(letter)
            
            if letter in secret:
                correct.append(letter)
                newguess = ""
                for i in range(0, len(secret)*2, 2):
                    if secret[i//2] == letter:
                        newguess += letter + " "
                    else:
                        newguess += guess[i:i+2]
                guess = newguess
                print("You have guessed the correct letter!")
                if "_" not in guess:
                    print("Congratulations! You have guessed the correct word!")
                    score['win'] += 1
                    break
            elif not letter.isalpha():
                print("Please input a LETTER!")
            else:
                print("Oops! You have not guessed the correct letter.")
                wrong_guesses += 1
                print(f"Wrong guesses left: {6 - wrong_guesses}")
            
            if wrong_guesses == 6:
                print("Sorry, you've run out of guesses. The word was: ", secret)
                score['lose'] += 1
                break
        
        #Untuk tanya ke user apakah mau melanjutkan game atau tidak
        play_again = input("Do you want to play again? (yes/no) ").lower()
        if play_again != "yes":
            break
    
    # Final score
    print(f"Final score -> Wins: {score['win']}, Losses: {score['lose']}")

if __name__ == "__main__":
    main()