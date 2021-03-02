# Given a list of words. find a list of words that are greater than 4 characters
words = ["hello", "goodbye", "merci", "but", "and", "oxford"]

result_list = []

counter = 0
while counter < 6:
    if len(words[counter]) > 4:
        result_list.append(words[counter])
    counter += 1

print("List of words greater than 4 characters:", result_list)
