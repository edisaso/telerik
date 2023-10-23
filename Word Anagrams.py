def is_anagram(word, candidate):
    return sorted(word) == sorted(candidate)

# Read the word to check against
word = input("Please enter the word to check against: ")

# Read the number of words in the list
n = int(input("Please enter the number of words in the list: "))

# Read the words from the list and check whether they are anagrams of the word
for _ in range(n):
    candidate = input("Please enter a word from the list: ")
    print("Yes" if is_anagram(word, candidate) else "No")