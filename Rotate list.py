def rotate_list(nums, N):
    N = N % len(nums)
    return nums[N:] + nums[:N]

if __name__ == '__main__':
    nums = input().strip().split(',')
    N = int(input().strip())
    result = rotate_list(nums, N)
    print(','.join(result))
