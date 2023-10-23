def title_search(title, lines):
    for line in lines:
        temp_title = title
        for char in line:
            if char in temp_title:
                temp_title = temp_title.replace(char, '', 1)
            else:
                print("No such title found!")
                break
        else:
            print(temp_title)

# Prompt the user to input a title and a list of lines
title = input("Please enter a title: ")
n = int(input("Please enter the number of lines: "))
lines = [input("Please enter a line: ") for _ in range(n)]

# Perform the title search and print the results
title_search(title, lines)
