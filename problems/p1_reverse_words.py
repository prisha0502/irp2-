# Problem 1: Reverse Word Order

sentence = input()
words = sentence.split()

reversed_words = words[::-1]

print(" ".join(reversed_words))
