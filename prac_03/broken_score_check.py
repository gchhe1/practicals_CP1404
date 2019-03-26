"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    """A score status is displayed"""
    score = float(input("Enter score: "))
    print(determine_status(score))


def determine_status(score):
    """determine the score after the user input"""

    if score < 0 or score > 100:
        return "Invalid score"

    elif score < 50:
        return "Bad"

    elif score >= 90:
        return "Excellent"

    else:
        return "Passable"


main()
