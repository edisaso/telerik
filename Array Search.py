def find_missing_elements(nums, N):
    full_set = set(range(1, N + 1))
    existing_set = set(nums)
    missing_elements = sorted(list(full_set - existing_set))
    return missing_elements

if __name__ == '__main__':
    nums = list(map(int, input().strip().split(',')))
    N = len(nums)
    result = find_missing_elements(nums, N)
    print(','.join(map(str, result)))