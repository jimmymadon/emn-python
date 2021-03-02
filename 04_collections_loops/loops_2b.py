# Given a list of words. find a list of words that are greater than 4 characters

# Ask user for 6 words that we can store in a list
# Manual repeating method
# word1= input("Please enter a word: ")
# word2 = input("Please enter a word: ")
# word3 = input("Please enter a word: ")
# word4 = input("Please enter a word: ")
# word5 = input("Please enter a word: ")
# word6 = input("Please enter a word: ")
# words = [word1, word2, word3, word4, word5, word6]

number_of_words = int(
    input("How many words do you want to enter? (Enter a number)"))

words = []
for count in range(number_of_words):
    word = input("Please enter a word: ")
    words.append(word)

result_list = []
for word in words:
    if len(word) > 4:
        result_list.append(word)

print("List of words greater than 4 characters:", result_list)
