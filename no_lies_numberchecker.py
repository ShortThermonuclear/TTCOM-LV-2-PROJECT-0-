def int_check(question):
    """Checks if the input is an integer or not"""

    error = "Please enter a valid age"

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print(error)

# Main routine


while True:

    print()

    name = input("Please enter your name:")

    if name == "":
        print("Please enter a valid name.")
        continue

    age = int_check("Please enter your age: ")
    print(f"Your age is {age}")

    if age < 12:
        print(f"{name} is too young.")
        continue

    elif age > 120:
        print(f"{name} is too old.")
        continue

    else:
        print("you successfully bought a ticket!")
