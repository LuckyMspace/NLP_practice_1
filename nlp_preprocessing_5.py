
# "Tokenization of sentences containing apostrophes.

from nltk.tokenize import WordPunctTokenizer


sentence = "it's nothing that you don't already know except most people aren't aware of how their inner world works."

words = WordPunctTokenizer().tokenize(sentence)
print(words)