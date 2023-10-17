def compare_arrays_lexicographically(array1, array2):
    if array1 < array2:
        return "first"
    elif array1 > array2:
        return "second"
    else:
        return "equal"

if __name__ == '__main__':
    array1 = input().strip()
    array2 = input().strip()
    print(compare_arrays_lexicographically(array1, array2))
