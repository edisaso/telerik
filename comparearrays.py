def compare_arrays():
    N = int(input())
    array1 = [int(input()) for _ in range(N)]
    array2 = [int(input()) for _ in range(N)]

    if array1 == array2:
        print("equal")
    else:
        print("not equal")

if __name__ == '__main__':
    compare_arrays()
