# Welcome Message
print("Welcome to Mastermind Game")
secret = [4, 1, 2, 3]

posCorrect = 0
guesses = 0
MaxGuesses = 15

while posCorrect < 4 and guesses < MaxGuesses:
    guessArrayString = input("Enter your guess of four numbers: ").split()
    guesses += 1

    guessArrayInt = [int(i) for i in guessArrayString]

    tempSecret = secret.copy()
    tempGuessInt = guessArrayInt.copy()
    colorsCorrect = 0
    posCorrect = 0

    for i in range(len(tempSecret)):
        if tempSecret[i] == tempGuessInt[i]:
            posCorrect += 1
            tempSecret[i] = -1
            tempGuessInt[i] = -1

    for i in range(len(tempSecret)):
        for j in range(len(tempGuessInt)):
            if tempSecret[i] != -1 and tempSecret[i] == tempGuessInt[j] and tempGuessInt[j] != -1:
                colorsCorrect += 1
                tempSecret[i] = -1
                tempGuessInt[j] = -1 
                break

    print("Positions Correct: ", posCorrect)
    print("Colors Correct: ", colorsCorrect)

    if posCorrect == 4:
        print("You Win")
    elif guesses == MaxGuesses:
        print("You Lose")

print("Secret combo was", secret)
