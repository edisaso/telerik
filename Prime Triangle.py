def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_triangle(n):
    for i in range(1, n + 1):
        if is_prime(i) or i == 1:
            print(''.join('1' if is_prime(j) or j == 1 else '0' for j in range(1, i + 1)))

# Prompt the user to input a number
n = int(input("Please enter a number: "))

# Print the prime triangle
prime_triangle(n)