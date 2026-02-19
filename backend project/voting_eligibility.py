# ============================================
# Voting Eligibility Checker
# ============================================

def check_voting_eligibility(age_input):
    """
    Check if a person is eligible to vote.
    
    Edge cases handled:
    - age = 18 (minimum voting age, eligible)
    - age negative (invalid input)
    - age as text/non-number (invalid input)
    """

    # Edge Case 3: Check if input is text (not a number)
    try:
        age = int(age_input)
    except ValueError:
        return "❌ Invalid input! Age must be a number, not text."

    # Edge Case 2: Check if age is negative
    if age < 0:
        return "❌ Invalid input! Age cannot be a negative number."

    # Edge Case 1: age = 18 (exactly 18 is eligible)
    # General check: Must be 18 or older to vote
    if age >= 18:
        return f"✅ Age {age}: You ARE eligible to vote!"
    else:
        return f"❌ Age {age}: You are NOT eligible to vote. You must be at least 18 years old."


# ============================================
# Main Program
# ============================================

print("=" * 45)
print("       VOTING ELIGIBILITY CHECKER")
print("=" * 45)

# --- Test the edge cases ---
print("\n📋 Running Edge Case Tests:")
print("-" * 45)

# Edge Case 1: age = 18
result = check_voting_eligibility(18)
print(f"Test (age = 18):       {result}")

# Edge Case 2: negative age
result = check_voting_eligibility(-5)
print(f"Test (age = -5):       {result}")

# Edge Case 3: text input
result = check_voting_eligibility("hello")
print(f"Test (age = 'hello'):  {result}")

print("-" * 45)

# --- Interactive Mode ---
print("\n🗳️  Enter your age to check eligibility.")
print("   (Type 'quit' to exit)\n")

while True:
    user_input = input("Enter age: ")

    if user_input.lower() == "quit":
        print("Goodbye! 👋")
        break

    result = check_voting_eligibility(user_input)
    print(result)
    print()