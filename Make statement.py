#Functions goes here
def make_statement(statement, decoration):
    """Makes the heading stand out more by adding decorations."""
    print(f"{decoration * 3} {statement} {decoration * 3}")

#Main routine goes here
make_statement("I like pizza", "🍕")
