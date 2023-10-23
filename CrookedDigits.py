def crooked_digit(n):
    n = str(n).replace('.', '').replace('-', '')
    if len(n) == 1:
        return int(n)
    else:
        return crooked_digit(sum(int(i) for i in n))
n = input("Please enter a number: ")
n = float(n) if '.' in n else int(n)
print(crooked_digit(n))