#6.	Program to count number of unique words in a given sentence using sets.

sentence = input("Enter a sentence: ")
words = sentence.split()
unique_words = set(words)
print("Number of unique words in the given sentence:", len(unique_words))
