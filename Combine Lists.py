def combine_lists(list1, list2):
    combined_list = [str(x) + "," + str(y) for x, y in zip(list1, list2)]
    return ",".join(combined_list)

if __name__ == '__main__':
    list1 = input().strip().split(',')
    list2 = input().strip().split(',')
    result = combine_lists(list1, list2)
    print(result)