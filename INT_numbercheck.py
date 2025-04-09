# Function goes here
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

    age = int_check("Please enter your age: ")
    print(f"Your age is {age}")
