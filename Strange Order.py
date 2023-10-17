def strange_order(numbers):
    negatives = sorted(filter(lambda x: x < 0, numbers))
    zeros = [x for x in numbers if x == 0]
    positives = sorted(filter(lambda x: x > 0, numbers))
    return ','.join(map(str, negatives + zeros + positives))

if __name__ == '__main__':
    numbers = list(map(int, input().strip().split(',')))
    result = strange_order(numbers)
    print(result)
