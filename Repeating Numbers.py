from collections import Counter

# Read the number of integers
n = int(input("Please enter the number of integers: "))

# Read the integers
numbers = [int(input("Please enter an integer: ")) for _ in range(n)]

# Count the occurrences of each integer and find the one that occurs the most times
counter = Counter(numbers)
max_count = max(counter.values())
most_common = [k for k, v in counter.items() if v == max_count]

# If there are two numbers that occur the same amount of times, return the smaller of the two
print(min(most_common))