"""
max_number_finder
A program to find and display the larger of two numbers provided by the user.
"""

def get_valid_input(prompt: str) -> float:
    """
    Prompts the user for a numeric input and validates it.

    Args:
        prompt (str): The message shown to the user to ask for input.

    Returns:
        float: A number entered by the user.

    Raises:
        ValueError: If the input is not a valid number.
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Please enter a valid number.")

def find_max_number(num1: float, num2: float) -> float:
    """
    Determines the larger of two numbers.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The larger of the two numbers.
    """
    return max(num1, num2)

def get_continue_choice() -> bool:
    """
    Prompts the user to decide whether to continue or exit the program.

    Returns:
        bool: True if the user wants to continue, False if they want to exit.

    Raises:
        KeyboardInterrupt: If the user interrupts the input.
    """
    while True:
        try:
            choice = input("\nDo you want to compare another pair of numbers? (yes(y)/no(n)): ").strip().lower()
            if choice in ('yes', 'y'):
                return True
            elif choice in ('no', 'n'):
                return False
            else:
                print("Error: Please enter 'yes(y)' or 'no(n)'.")
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            return False

def max_number_finder():
    """
    Prompts the user for two numbers, finds and displays the larger one.
    Handles input validation to prevent crashes from invalid entries.
    Allows the user to continue comparing or exit.
    """
    print("\nMax Number Finder is RUNNING")

    while True:
        print("Please Enter Two Numbers to Compare\n")
        try:
            num1 = get_valid_input("Enter the first number: ")
            num2 = get_valid_input("Enter the second number: ")

            max_num = find_max_number(num1, num2)

            print(f"\nFirst Number: {num1}")
            print(f"Second Number: {num2}\n")
            print(f"Larger Number: {max_num}")

            if not get_continue_choice():
                print("\nThank you for using Max Number Finder. Goodbye!")
                break

        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    max_number_finder()