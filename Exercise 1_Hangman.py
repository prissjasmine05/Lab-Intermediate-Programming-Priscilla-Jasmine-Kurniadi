def main ():
    secret_word = "hangman"
    guess = "_ " *len(secret_word)
    correct = []
    print ("The word have",len(secret_word),"letters")

    while True:
        print ("Guess this",guess)
        letter = input("Guess a letter: ").lower()
        if letter in secret_word:
            correct.append(letter)
            newguess = ""
            for i in range(len(secret_word)):
                if secret_word[i] == letter:
                    newguess += letter
                else:
                    newguess += guess[i]
            guess = newguess
            print("You have guessed the correct letter")
            if "_" not in guess:
                print("Congratulations! You have guessed the correct word!")
                break
        elif not letter.isalpha():
            print("Please input a letter")
        else:
            print("Oops! You have not guessed the correct letter")

main()