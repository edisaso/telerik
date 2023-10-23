def is_balanced(n):
    n = str(n)
    return int(n[1]) == int(n[0]) + int(n[2])

def sum_balanced_numbers():
    total = 0
    while True:
        n = int(input("Please enter a 3-digit number: "))
        if is_balanced(n):
            total += n
        else:
            break
    return total

# Test the function
print(sum_balanced_numbers())