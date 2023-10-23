def game(n):
    digits = [int(d) for d in str(n)]
    return max(digits[0] + digits[1] * digits[2], digits[0] * digits[1] + digits[2])

# Prompt the user to input a 3-digit number
n = int(input("Please enter a 3-digit number: "))

# Calculate and print the biggest number
print(game(n))