# Using accumulator and if statements
print("-------------------------------")
print("Welcome to the Trivia Challenge!")
print("80's Trivia")
score = 0
# Asking Questions
# First Question and If statement and I am using the upper case method to avoid syntax errors.
# I also casted every response to default string to avoid syntax errors
question_one = input("What is the name of the princess who is kidnapped by the evil Bowser in multiple Mario video games?: ")
if question_one.upper() == "PEACH" and score == 0:
    score += 1
    print(f'Yay! You got this!!\nYour score is {score} out of 5')
else:
    print(f'Incorrect. The correct answer is Peach\nYour score is {score} out of 5')

# Second Question and If else statement and I am using the upper case method to avoid syntax errors
# I also casted every response to default string to avoid syntax errors
question_two = input("What year in the 80s did the Berlin wall come down?: ")
if question_two.upper() == "1982":
    score += 1
    print(f'Yay! You got this!!\nYour score is {score} out of 5')
else:
    print(f'Incorrect. The correct answer is 1982\nYour score is {score} out of 5')

# Third Question and If else statement and I am using the upper case method to avoid syntax errors
# I also casted every response to default string to avoid syntax errors
question_three = input("What is the name of the Apatosaurus in 'The Land Before Time'?: ")
if question_three.upper() == "LITTLEFOOT":
    score += 1
    print(f'Yay! You got this!!\nYour score is {score} out of 5')
else:
    print(f'Incorrect. The correct answer is Littlefoot\nYour score is {score} out of 5')

# Fourth Question and If else statement and I am using the upper case method to avoid syntax errors
question_four = input("Who is credited with the invention of the Internet in 1989?: ")
if question_four.upper() == "TIM BERNERS-LEE":
    score += 1
    print(f'Yay, you got this!!\nYour score is {score} out of 5')
else:
    print(f'Incorrect. The correct answer is Tim Berners-Lee')

# Fifth Question and If else statement. and I am using the upper case method to avoid syntax errors
# I also casted every response to default string to avoid syntax errors
question_five = input("In Back to the Future (1985), which year do Marty and Doc end up in when they travel back in time?: ")
if question_five.upper() == "1955":
    score += 1
    print(f'Yay, you got this!!\nYour score is {score} out of 5')
else:
    print(f'Incorrect. The correct answer is 1955\nYour Best Score is {score} out of 5')