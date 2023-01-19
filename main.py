

import random

destinations_list = ["Chicago","New York City","Orlando","Los Angeles"]

restaurants_list_new_york = ["Carmine's","Balthazar","Buddakan","Keens's Steakhouse"]

restaurants_list_orlando = ["The Melting Pot", "Hard Rock Cafe","Maggiano's","Charley's Steakhouse"]

restaurants_list_chicago = ["Giordanos","Lou Malnatis","Gibsons Bar & Steakhouse","Frontera Grill"]

restaurants_list_los_angeles = ["Bottega Louie","Musso and Frank Grill","Providence","Bestia"]

transportation_list = ["Train","Car","Walking","Bike"]

entertainment_list_chicago = ["Millennium Park","Museum of Contemporary Art","Grant Park","Promontory Point"]

entertainment_list_new_york = ["Central Park","Frick Collection","Conservatory Garden","St. Patrick's Cathedral"]

entertainment_list_orlando = ["Disney World","Sea World","Universal Studios","Discovery Cove"]

entertainment_list_los_angeles = ["Getty Center","Griffith Park","Universal Studios","Hollywood Sign"]


print("Welcome to Day Trip Generator. Vacation plans in just a few minutes!")

user_input = ""


while user_input != "y":
    destination = random.choice(destinations_list)
    user_input = input(f"Your destination is {(destination)}. Does this sound good? y/n")

user_input = ""

if destination == "Chicago":
    while user_input != "y":
        restaurant = random.choice(restaurants_list_chicago)
        user_input = input(f"Your restaurant is {(restaurant)}. Does this sound good? y/n")
elif destination == "New York City":
    while user_input != "y":
        restaurant = random.choice(restaurants_list_new_york)
        user_input = input(f"Your restaurant is {(restaurant)}. Does this sound good? y/n")
elif destination == "Orlando":
    while user_input != "y":
        restaurant = random.choice(restaurants_list_orlando)
        user_input = input(f"Your restaurant is {(restaurant)}. Does this sound good? y/n")
elif destination == "Los Angeles":
    while user_input != "y":
        restaurant = random.choice(restaurants_list_los_angeles)
        user_input = input(f"Your restaurant is {(restaurant)}. Does this sound good? y/n")

user_input = ""

if destination == "Chicago":
    while user_input != "y":
        entertainment = random.choice(entertainment_list_chicago)  
        user_input = input(f"Your entertainment is {(entertainment)}. Does this sound good? y/n")
elif destination == "New York City":
    while user_input != "y":
        entertainment = random.choice(entertainment_list_new_york)
        user_input = input(f"Your entertainment is {(entertainment)}. Does this sound good? y/n")
elif destination == "Orlando":
    while user_input != "y":
        entertainment = random.choice(entertainment_list_orlando)
        user_input = input(f"Your entertainment is {(entertainment)}. Does this sound good? y/n")
elif destination == "Los Angeles":
    while user_input != "y":
        entertainment = random.choice(entertainment_list_los_angeles)
        user_input = input(f"Your entertainment is {(entertainment)}. Does this sound good? y/n")
 
user_input = ""

while user_input != "y":
    transportation = random.choice(transportation_list)
    user_input = input(f"Your transportation is {(transportation)}. Does this sound good? y/n")

user_input = ""


print(f"You will be traveling to {(destination)}, experiencing {(entertainment)}. Traveling via {(transportation)} and ending the night dining at {(restaurant)}.")