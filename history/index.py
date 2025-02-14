score = 0

# Question 1
options_Q1 = [
    "1. Guido van Rossum",
    "2. James Gosling",
    "3. Bjarne Stroustrup",
    "4. Dennis Ritchie"
]

while True:
    print("\nWho is the inventor of Python?")
    for option in options_Q1:
        print(option)

    choose = input("Choose the number corresponding to your option: ")

    if choose == "1":
        print("You are correct!")
        score += 1
        break
    else:
        print("That's incorrect.")
        retry = input("Do you want to try again? (yes/no): ").lower()
        if retry != 'yes':
            break

# Question 2
options_Q2 = [
    "1. After a snake",
    "2. After a bird",
    "3. After a fish",
    "4. After a mammal"
]

while True:
    print("\nWhy was Python named Python?")
    for option in options_Q2:
        print(option)

    choose = input("Choose the number corresponding to your option: ")

    if choose == "1":
        print("You are correct!")
        score += 1
        break
    else:
        print("That's incorrect.")
        retry = input("Do you want to try again? (yes/no): ").lower()
        if retry != 'yes':
            break

# Question 3
options_Q3 = [
    "1. 1989",
    "2. 1990",
    "3. 1991",
    "4. 1992"
]

while True:
    print("\nWhen was Python created?")
    for option in options_Q3:
        print(option)

    choose = input("Choose the number corresponding to your option: ")

    if choose == "2":
        print("You are correct!")
        score += 1
        break
    else:
        print("That's incorrect.")
        retry = input("Do you want to try again? (yes/no): ").lower()
        if retry != 'yes':
            break

# Question 4
options_Q4 = [
    "1. Windows",
    "2. Mac",
    "3. Linux",
    "4. All of the above"
]

while True:
    print("\nWhat platform did Python support?")
    for option in options_Q4:
        print(option)

    choose = input("Choose the number corresponding to your option: ")

    if choose == "4":
        print("You are correct!")
        score += 1
        break
    else:
        print("That's incorrect.")
        retry = input("Do you want to try again? (yes/no): ").lower()
        if retry != 'yes':
            break

# Question 5
options_Q5 = [
    "1. 2.7",
    "2. 3.0",
    "3. 3.6",
    "4. 3.7"
]

while True:
    print("\nWhat is the current version of Python?")
    for option in options_Q5:
        print(option)

    choose = input("Choose the number corresponding to your option: ")

    if choose == "4":
        print("You are correct!")
        score += 1
        break
    else:
        print("That's incorrect.")
        retry = input("Do you want to try again? (yes/no): ").lower()
        if retry != 'yes':
            break

# Final Score Display
print(f"\nYour final score is: {score}/5")

if score == 5:
    print("Excellent! You got all the answers correct!")
elif score >= 3:
    print("Good job! You know quite a bit about Python.")
else:
    print("Keep practicing! You'll get better.")
