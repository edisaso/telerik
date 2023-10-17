def negative_positive_sort(nums):
    negative_nums = [x for x in nums if x < 0]
    positive_nums = [x for x in nums if x >= 0]
    return negative_nums + positive_nums

if __name__ == '__main__':
    nums = list(map(int, input().strip().split()))
    result = negative_positive_sort(nums)
    print(' '.join(map(str, result)))
