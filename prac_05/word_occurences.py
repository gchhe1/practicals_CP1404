word_counter = {}
text = input("Text: ")


words = text.split()
for word in words:
    frequency = word_counter.get(word, 0)
    word_counter[word] = frequency + 1

words = list(word_counter.keys())
words.sort()
word_length = max((len(word) for word in words))

for word in words:
    print("{:{}} : {}".format(word, word_length, word_counter[word]))