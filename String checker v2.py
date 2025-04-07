# Function goes here
def string_check(question, list_1, num_letters):
    """Checks if the user enters the first letter or a full word from a list of words """

    while True:
        response = input(question).lower()

        for item in list_1:
            if response == item:
                return item
            elif response == item[:num_letters]:
                return item
            # checks if user enters valid item and responds correctly.
        else:
            print(f"Please chose a valid vehicle.")
        # Prints an error message in the case of invalid input


# Main routine goes here
Vehicles = ['car', 'cycle', 'motorcycle']
vehicle_transport = string_check("How do u travel to school ", Vehicles, 2)
print(f"You chose {vehicle_transport}")
