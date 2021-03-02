# Given a list of words. find a list of words that are greater than 4 characters

# Create a while loop like in loops_2c.py
words = []
counter = 0
while counter < 1000:
    word = input("Please enter a word (or Q to exit): ")
    if word == "Q":
        break
    words.append(word)
    counter += 1

result_list = []
counter = 0
while counter < len(words):
    if len(words[counter]) > 4:
        result_list.append(words[counter])
    counter += 1

print("List of words greater than 4 characters:", result_list)
