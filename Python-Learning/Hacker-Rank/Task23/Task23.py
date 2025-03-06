import re
def is_valid_credit_card(card):
    # Check if the format is valid (either all digits or grouped with '-')
    valid_format = re.fullmatch(r'^[456]\d{3}(-?\d{4}){3}$', card)
    if not valid_format:
        return "Invalid"

    # Remove hyphens for further validation
    card_digits = card.replace("-", "")

    # Check for 4 or more consecutive repeated digits
    if re.search(r'(\d)\1{3,}', card_digits):
        return "Invalid"

    return "Valid"

# Read input
N = int(input().strip())
for _ in range(N):
    card_number = input().strip()
    print(is_valid_credit_card(card_number))
