
# Given a sentence from the user, print the longest word in the sentence

sentence = input("sentence: ")

words = sentence.split()
longest_word = ''

for i in range(len(words)):
    try:
        if len(words[i]) > len(words[i+1]):
            largest = words[i]
    except Exception:
        largest = words[i]

print(longest_word)
