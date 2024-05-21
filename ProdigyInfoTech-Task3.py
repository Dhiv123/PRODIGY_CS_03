import re
import random

def assess_password_strength(password):
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    digit_criteria = re.search(r'[0-9]', password) is not None
    special_criteria = re.search(r'[\W_]', password) is not None

    criteria_met = sum([length_criteria, lowercase_criteria, uppercase_criteria, digit_criteria, special_criteria])

    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Medium"
    elif criteria_met == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    feedback = {
        "length_criteria": length_criteria,
        "lowercase_criteria": lowercase_criteria,
        "uppercase_criteria": uppercase_criteria,
        "digit_criteria": digit_criteria,
        "special_criteria": special_criteria,
        "strength": strength
    }

    return feedback

def fact():
    facts = [
        "A strong password is your first line of defense against cyber attacks.",
        "Always use a combination of letters, numbers, and special characters in your passwords.",
        "Consider using a password manager to keep track of your strong passwords.",
        "Changing your passwords regularly can significantly increase your security.",
        "Never share your passwords with others to maintain account security."
    ]
    return random.choice(facts)

def main():
    print("*********************************************************************************")
    print(" ")
    print("  Welcome to the Cybersecurity Password Complexity Assessment Tool!")
    print(" ")
    print("*********************************************************************************")
    while True:
        password = input("\nEnter a password to assess (or 'q' to quit): ")

        if password.lower() == 'q':
            print("*********************************************************************************")
            print(" ")
            print("Exiting the Password Complexity Assessment Tool. Stay secure!")
            print(" ")
            print("*********************************************************************************")
            break

        feedback = assess_password_strength(password)
        print("\n*********************************************************************************")
        print(f"Password Strength: {feedback['strength']}")
        print("Criteria met:")
        print(f" - Length >= 8 characters: {'✔️' if feedback['length_criteria'] else '❌'}")
        print(f" - Contains lowercase letters: {'✔️' if feedback['lowercase_criteria'] else '❌'}")
        print(f" - Contains uppercase letters: {'✔️' if feedback['uppercase_criteria'] else '❌'}")
        print(f" - Contains digits: {'✔️' if feedback['digit_criteria'] else '❌'}")
        print(f" - Contains special characters: {'✔️' if feedback['special_criteria'] else '❌'}")
        print("*********************************************************************************")

        print("\nCybersecurity Tip:")
        print(f"{fact()}")
        print("\n")

if __name__ == "__main__":
    main()
