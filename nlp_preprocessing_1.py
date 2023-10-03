import nltk
nltk.download()
text = nltk.word_tokenize("Is it possible for me to study the field of natural language processing?")

text # 결과 확인

''' nltk downloader에서 identifier에서 all,all-corpora, all-nltk, book, popular 체크
이후 왼쪽 하단 download'''

nltk.download('averaged_perceptron_tagger')  # 태깅에 필요한 자원 다운로드

nltk.pos_tag(text)  # 품사 태깅

# VBZ: Verb, 3rd person singular present - 현재 시제의 동사 (세 번째 인칭 단수 형태). 예: "He runs."
# PRP: Personal pronoun - 인칭 대명사. 예: "he", "she", "they"
# JJ: Adjective - 형용사. 예: "happy", "sad"
# VBG: Verb, gerund or present participle - 동사의 현재분사 또는 동명사 형태. 예: "running", "thinking"
# NNS: Noun, plural - 명사의 복수형. 예: "cats", "dogs"
# CC: Coordinating conjunction - 등위 접속사. 예: "and", "or", "but"
