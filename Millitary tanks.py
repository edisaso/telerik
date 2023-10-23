def tank_position(moves):
    x, y = 0, 0
    for move in moves:
        if move == 'R':
            x += 1
        elif move == 'L':
            x -= 1
        elif move == 'U':
            y += 1
        elif move == 'D':
            y -= 1
    return (x, y)

# Prompt the user to input a sequence of moves
moves = input("Please enter a sequence of moves (R, L, U, D): ")

# Calculate and print the tank's coordinates
print(tank_position(moves))
