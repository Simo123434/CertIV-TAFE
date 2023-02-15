'''
ICTPRG Week 3 Homework

Author : Dylan Wondal

Project: Coffee or tea
    Ask user ig they want coffee or tea. 
    They can only have one or the other. 
    Then ask if they want milk and/or sugar.
    Maximum of 3 sugars otherwise doctor said to many.
    Repeat order to user.
'''
# Function to ask the user what drink they want.
def getDrinkChoice():
    print('What would you like to order?')
    print('Coffee - 1')
    print('Tea - 2')
    print('None - 3')
    choiceOfDrink = input("Enter Choice: ")
    # Check if input is a number.
    if choiceOfDrink.isnumeric():
        choiceOfDrink = int(choiceOfDrink)
    # Return invalid choice and try again.
    while choiceOfDrink!= 1 and choiceOfDrink!= 2 and choiceOfDrink!= 3:
        print('Please enter a valid option. \n')
        print('Coffee - 1')
        print('Tea - 2')
        choiceOfDrink = input("Enter Choice: ")
        if choiceOfDrink.isnumeric():
            choiceOfDrink = int(choiceOfDrink)
    # Return the users choice
    if choiceOfDrink == 1:
        drink = 'coffee'
        return drink
    elif choiceOfDrink == 2:
        drink = 'tea'
        return drink
    # If user doesn't want a drink, exit the program.
    elif choiceOfDrink == 3:
        print("Goodbye!")
        exit()

# Function to ask the user if they want milk. Uses same concept as getDrinkChoice.
def milk(drink):
    print(f'Would like milk with your {drink}?')
    print('Yes - 1')
    print('No - 2')
    milk = input("Enter Choice: ")
    if milk.isnumeric():
        milk = int(milk)
    while milk!= 1 and milk!= 2:
        print('Please enter a valid option. \n')
        print('Yes - 1')
        print('No - 2')
        milk = input("Enter Choice: ")
        if milk.isnumeric():
            milk = int(milk)
    if milk == 1:
        return True
    elif milk == 2:
        return False
        
# Function to ask the user if they want sugar. Uses same concept as getDrinkChoice.
def sugar(drink):
    print(f'Would like sugar with your {drink}?')
    print('Yes - 1')
    print('No - 2')
    sugar = input("Enter Choice: ")
    if sugar.isnumeric():
        sugar = int(sugar)
    while sugar!= 1 and sugar!= 2:
        print('Please enter a valid option. \n')
        print('Yes - 1')
        print('No - 2')
        sugar = input("Enter Choice: ")
        if sugar.isnumeric():
            sugar = int(sugar)
    if sugar == 1:
        print('How many sugars would you like?')
        print('Sugars available: 1-5')
        numOfSugars = input("Enter Choice: ")
        if numOfSugars.isnumeric():
            numOfSugars = int(numOfSugars)
        else:
            print("Please enter a valid option. \n")
            print('How many sugars would you like?')
            print('Sugars available: 1-5')
            numOfSugars = input("Enter Choice: ")
            if numOfSugars.isnumeric():
                numOfSugars = int(numOfSugars)
        # Checks to see if the number of sugars is greater than 3.
        if numOfSugars > 3:
            print("Too many sugars. DOCTOR SAYS TOO MANY!!!!! YOU GET NONE")
            return 0
        elif numOfSugars == 1:
            return 1
        elif numOfSugars == 2:
            return 2
        elif numOfSugars == 3:
            return 3
    if sugar == 2:
        return 0

# Main function that combines all the other functions and returns user's order.
def main():
    print('Welcome to the C0ffeE Sh0p!')
    drink = getDrinkChoice()
    isHavingMilk = milk(drink)
    isHavingSugar = sugar(drink)
    print(f"User is having {drink} with {'milk' if isHavingMilk else 'no milk'} and {isHavingSugar} sugar{'' if isHavingSugar == 1 else 's'}.")
    exit()


if __name__ == '__main__':
    main()