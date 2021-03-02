# Given a list of words. find a list of words that are greater than 4 characters

words = []
for count in range(1000):
    word = input("Please enter a word (or Q to exit): ")
    if word == "Q":
        break
    words.append(word)

result_list = []
for word in words:
    if len(word) > 4:
        result_list.append(word)

print("List of words greater than 4 characters:", result_list)
