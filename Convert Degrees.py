def celsius_to_fahrenheit(celsius):
    return round((celsius * 9/5) + 32)

if __name__ == '__main__':
    temperatures = list(map(int, input().strip().split()))
    for temp in temperatures:
        print(celsius_to_fahrenheit(temp))
