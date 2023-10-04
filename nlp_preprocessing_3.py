
# sentence tokenization

from nltk import sent_tokenize
text_sample = 'Natural Language Processing, or NLP, is the process of extracting the meaning, or intent, behind human language. In the field of Conversational artificial intelligence (AI), NLP allows machines and applications to understand the intent of human language inputs, and the generate appropriate responses, resulting in a natural conversation flow.'

tokenized_sentences = sent_tokenize(text_sample)
print(tokenized_sentences)
