#Program to display a restaurant menu and take user input to select an item from the menu
print("Welcome to the Restaurant Menu")
print("What would you like to have?")
print("1. Breakfast")
print("2. Lunch")
print("3. Dinner")
print("4. Exit")

user_choice = int(input("Enter your choice: "))

# Define menu items and prices
menus = {
    1: {
        "name": "Breakfast",
        "items": ["Eggs and Toast", "Cheese Sandwiches", "Tea and Bread", "Coffee and Donuts"],
        "prices": [150, 200, 100, 250]
    },
    2: {
        "name": "Lunch",
        "items": ["Chicken Biryani", "Salad", "Rice", "Vegetable Soup"],
        "prices": [300, 350, 400, 450]
    },
    3: {
        "name": "Dinner",
        "items": ["Chicken Spaghetti", "Cheese Burger", "Vegetable Pasta", "Roasted Chicken"],
        "prices": [500, 550, 600, 650]
    }
}

if user_choice in menus:
    print("Here is your " + menus[user_choice]["name"] + " Menu:")
    for i in range(len(menus[user_choice]["items"])):
        print(str(i + 1) + ". " + menus[user_choice]["items"][i] + " - PKR " + str(menus[user_choice]["prices"][i]))
    print("5. Exit")

    item_choice = int(input("Enter your choice: "))

    if 1 <= item_choice <= 4:
        selected_item = menus[user_choice]["items"][item_choice - 1]
        selected_price = menus[user_choice]["prices"][item_choice - 1]

        print("You have selected:", selected_item)
        print("Price: PKR", selected_price)

    elif item_choice == 5 or user_choice == 4:
        print("Thank you for visiting our restaurant!")

    else:
        print("Invalid choice. Please enter a valid option.")

    print("Thanks for visiting us. Have a great day!")

