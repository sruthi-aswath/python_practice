Word Frequency Counter-
# Given a sentence, count how many times each word appears.

sentence = "apple banana apple orange banana apple"

individual_words = sentence.split()
print(individual_words)

word_count = {}
for word in individual_words:
    if word in word_count:
         word_count[word] += 1
    else:
        word_count[word] = 1
   
print(word_count)