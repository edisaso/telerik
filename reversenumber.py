def reverse_number(number):
    return str(number)[::-1]

if __name__ == '__main__':
    num = input().strip()
    print(reverse_number(num))