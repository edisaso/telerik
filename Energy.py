def energy_drink(n):
    n = str(n)
    even_sum = sum(int(digit) for digit in n if int(digit) % 2 == 0)
    odd_sum = sum(int(digit) for digit in n if int(digit) % 2 != 0)

    if even_sum > odd_sum:
        return f"energy drinks {even_sum}"
    elif odd_sum > even_sum:
        return f"cups of coffee {odd_sum}"
    else:
        return f"both {even_sum}"

# Prompt the user to input a number
n = int(input("Please enter a number: "))

# Calculate and print the kind of beverage you should drink
print(energy_drink(n))