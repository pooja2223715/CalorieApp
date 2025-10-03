# Step 1: Restaurant data
restaurants = {
    "Cafe A": {"Salad": 150, "Sandwich": 300, "Juice": 100},
    "Bistro B": {"Burger": 500, "Soup": 200, "Coffee": 50},
    "Deli C": {"Wrap": 350, "Smoothie": 180, "Cookie": 120}
}

# Step 2: Take user input
calorie_limit = int(input("Enter your calorie limit: "))

# Step 3: Suggest meals under calorie limit
print("\nMeals you can eat within your limit:")

for restaurant, items in restaurants.items():
    for item, calories in items.items():
        if calories <= calorie_limit:
            print(f"{item} at {restaurant} ({calories} cal)")
