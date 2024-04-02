import os

while True:
    
    secret_word = input("Enter the secret word: ")
    secret_word_nospace = secret_word.replace(" ", "")

    list_attempts = [7, 14, 28, 35]
    def_attempts = input(f"Define the number of attempts {list_attempts}: ")
    def_attempts_int = int(def_attempts)
    attempts = 0 

    if def_attempts_int not in list_attempts:
        os.system("cls")
        print("You choose a invalid number")
        print(f"Choose a number from the options")
        print()
        def_attempts = input(f"Define the number of attempts {list_attempts}: ")

    if secret_word_nospace.isalpha() and len(secret_word_nospace) > 1:
        os.system("cls")

        while attempts != def_attempts_int:
            print("HANGMAN'S NOOSE GAME")
            print()
            print("|¨¨¨|")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
            print(f"Attempts: {attempts}/{def_attempts}")
            print()
            typed_letters = input("Enter a letter: ")
            attempts += 1
            print('EITA')
            if typed_letters in secret_word:
                os.system("cls")
                print("Acertou")
                continue
            else:
                os.system("cls")
                continue
            

        if attempts == def_attempts_int:
            print("Acabou")


    else:
        os.system("cls")
        print(f"ERROR: you entered a number ({secret_word})")
        print("Please, type in a word that contains only letters")
        print()
        continue
    
    
    
    break

    # print("|¨¨¨|")
    # print("|")
    # print("|")
    # print("|")
    # print("|")
    # print("|")
    # print("|")
    


# print("|¨¨¨|")
# print("|   O   ")
# print(r"|  /|\ ")
# print("|   |   ")
# print(r"|  / \  ")
# print("|")
# print("|")


