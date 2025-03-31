# Functions go here
def yes_no(question):
    """Checks that if the user entered yes/y or no/n."""

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter yes or no. \n")

# Main routine goes here
while True:
    want_instructions = yes_no("Do u want to read the instructions?")
    print(f"You chose {want_instructions}\n")
