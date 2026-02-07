# Input a sentence and print words in separate lines.
sentence = input("Enter a sentence: ")
words = sentence.split()
print("Words in the given sentence:")
for word in words:
    print(word)
