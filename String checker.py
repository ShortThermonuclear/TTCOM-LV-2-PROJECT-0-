# Function goes here
def string_check(question, list_1):
    """Checks if the user enters the first letter or a full word from a list of words """

    while True:
        response = input(question).lower()

        for item in list_1:
            if response == item:
                return item
            elif response == item[0]:
                return item
            else:
                print(f"Please enter a valid input from {list_1}")


# Main routine goes here
Vehicles = ['car', 'bus', 'motorcycle']
vehicle_transport = string_check("How do u travel to school ", Vehicles)
print(f"You chose {vehicle_transport}")
