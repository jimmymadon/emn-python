# Given a list of words. find a list of words that are greater than 4 characters
words = ["hello", "goodbye", "merci", "but", "and", "oxford"]

result_list = []
for word in words:
    if len(word) > 4:
        result_list.append(word)

print("List of words greater than 4 characters:", result_list)
