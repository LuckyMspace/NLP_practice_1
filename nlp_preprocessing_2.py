import nltk


nltk.download('punkt')  # 문장을 단어로 쪼개기 위한 자원
string1 = "my favorite sports is swim meat"
string2 = "my favorite sports is swim meat, crossfit, badminton."
nltk.word_tokenize(string1)
nltk.word_tokenize(string2)


# KoNLpy는 추후에
