# Voting Eligibility Checker

print("=== Voting Eligibility Checker ===")

age_input = input("Enter your age: ")

# Edge case: age is text (not a number)
if not age_input.isdigit():
    print("Invalid input! Please enter a valid number.")
else:
    age = int(age_input)

    # Edge case: age is negative
    if age < 0:
        print("Invalid age! Age cannot be negative.")

    # Edge case: age is exactly 18
    elif age == 18:
        print("Congratulations! You just turned 18, you are eligible to vote!")

    elif age >= 18:
        print("You are eligible to vote!")

    else:
        print("Sorry, you are not eligible to vote yet.")