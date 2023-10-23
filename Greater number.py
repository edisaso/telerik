def next_greater_number(first_array, second_array):
    result = []
    for num in first_array:
        index = second_array.index(num)
        next_greater = next((x for x in second_array[index:] if x > num), -1)
        result.append(next_greater)
    return result

# Prompt the user to input two arrays
first_array = list(map(int, input("Please enter the first array of numbers separated by commas: ").split(',')))
second_array = list(map(int, input("Please enter the second array of numbers separated by commas: ").split(',')))

# Calculate and print the next greater number for each number in the first array
print(next_greater_number(first_array, second_array))