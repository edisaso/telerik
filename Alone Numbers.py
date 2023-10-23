def alone_numbers(arr, target):
    for i in range(1, len(arr) - 1):
        if arr[i] == target and arr[i-1] != target and arr[i+1] != target:
            arr[i] = max(arr[i-1], arr[i+1])
    return arr

# Prompt the user to input an array and a target
arr = list(map(int, input("Please enter an array of integers separated by commas: ").split(',')))
target = int(input("Please enter the target: "))

# Calculate and print the new version of the array
print(alone_numbers(arr, target))
