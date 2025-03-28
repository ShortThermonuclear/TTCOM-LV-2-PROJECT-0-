# Functions goes here
def make_statement(statement, decoration, lines=1):
    """Creating heading(3 lines) , Subheadings(2 lines) and texts emphasised with decorations( 1 line)"""

    middle = f"{decoration * 3} {statement} {decoration * 3}"
    top_bottom = decoration * len(middle)

    if lines == 1:
        print(middle)

    elif lines == 2:
        print(middle)
        print(top_bottom)

    else:
        print(top_bottom)
        print(middle)
        print(top_bottom)


# Main routine goes here
make_statement("I like pizza", "🍕")
make_statement("Burger is also tasty", "-", 2)
make_statement(" Favorite Food", "*", 3)
