from random import randint 


def menu():
    print("1. EASY 1-10")
    print("2. MEDIUM 1-20")
    print("3. Hard 1-50")
    print("4. QUIT game")
menu()
user_choice = int(input("Choose a level: "))
    
def one():
    num = randint(1,10)   
    guess = int(input("Pick a number 1-10: "))
    number_of_guesses = 0
    while number_of_guesses <=3:
        if guess > num:
            print("Too high")
            guess = int(input("Pick a number 1-10: "))
        elif guess < num:
            print("Too low")
            guess = int(input("Pick a number 1-10: "))
        elif guess == num:
            print("You guessed correctly good job")
            break
        else:
            print("Nice try you get it next time")
        number_of_guesses +=1
def two():
    num = randint(1,20)
    guess = int(input("Pick a number 1-20: "))
    number_of_guesses = 0
    while number_of_guesses <=3:
        if guess > num:
            print("too high")
        elif guess < num:
            print ("too low")
            guess = int(input("Pick a number 1-20: "))
        elif guess == num:
            print("You guessed correctly good job")
            break
        else:
            print("Nice try you get it next time")
        number_of_guesses +=1
def three():
    num = randint(1,50)
    guess = int(input("Pick a number 1-50: "))
    number_of_guesses = 0
    while number_of_guesses <=3:
        if guess > num:
            print("too high")
            guess = int(input("Pick a number 1-50: "))
        elif guess < num:
            print ("too low")
            guess = int(input("Pick a number 1-50: "))
        elif guess == num:
            print("You guessed correctly good job")
            break
        else:
            print("Nice try you get it next time")
        number_of_guesses +=1                 
while user_choice !=5:
    if user_choice ==1:
        one()
        menu()
        user_choice = int(input("Choose a level: " ))
    elif user_choice ==2:
        two()
        menu()
        user_choice = int(input("Choose a level: " ))
    elif user_choice ==3:
        three()
        menu()
        user_choice = int(input("Choose a level: " ))
    else:
        print("Thank you for playing")
        break