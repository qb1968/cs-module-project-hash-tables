import random
import markovify

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
text_model = markovify.Text(words)

for i in range(5):
    print(text_model.make_sentence())

for i in range(3):
    print(text_model.make_short_sentence(100))

# TODO: construct 5 random sentences
# Your code here

