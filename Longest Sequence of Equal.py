def find_max_sequence_length(N, arr):
    max_length = 1
    current_length = 1

    for i in range(1, N):
        if arr[i] == arr[i - 1]:
            current_length += 1
            if current_length > max_length:
                max_length = current_length
        else:
            current_length = 1

    return max_length

if __name__ == '__main__':
    N = int(input())
    arr = [int(input()) for _ in range(N)]
    result = find_max_sequence_length(N, arr)
    print(result)
