file_path = "books/frankenstein.txt"

with open(file_path) as f:
    file_contents = f.read()

word_count = len(file_contents.split())

char_dictionary = {}

for char in file_contents:
    if not char.lower() in char_dictionary:
        char_dictionary[char.lower()] = 1
    else:
        char_dictionary[char.lower()] += 1

print(F"-- Begin report of {file_path} ---")
print(F"{word_count} words found in the document \n")

for key in char_dictionary:
    print(f"The '{key}' character was found {char_dictionary[key]} times")