def merge_and_squash(n, numbers):
    merged = []
    squashed = []
    for i in range(n - 1):
        a, b = numbers[i], numbers[i + 1]
        merged.append(int(str(a)[1] + str(b)[0]))
        squashed.append(int(str(a)[0] + str((int(str(a)[1]) + int(str(b)[0])) % 10) + str(b)[1]))
    return merged, squashed

# Prompt the user to input a number
n = int(input("Please enter the number of two-digit numbers: "))
numbers = [int(input("Please enter a two-digit number: ")) for _ in range(n)]

# Calculate and print the merged and squashed numbers
merged, squashed = merge_and_squash(n, numbers)
print(' '.join(map(str, merged)))
print(' '.join(map(str, squashed)))
