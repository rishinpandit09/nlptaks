import nltk
from nltk.stem import PorterStemmer
sp1 = PorterStemmer()
f = open("sample.txt", "r")
str1 = f.read()
str1 = [sp1.stem(token) for token in str1.split(" ")]
print(" ".join(str1))
#



from nltk.stem import LancasterStemmer
sp2 = LancasterStemmer()
str2 = str1
str2 = [sp2.stem(token) for token in str2.split(" ")]
print(" ".join(str2))

# from nltk.stem import RegexpStemmer
# sp3 = RegexpStemmer()
# str3 =
from nltk.stem import SnowballStemmer
# SnowballStemmer.languages
fs = SnowballStemmer('french')
print(fs.stem("manges"))

from nltk.stem import WordNetLemmatizer
lemma = WordNetLemmatizer()
print(lemma.lemmatize("cacti"))
print(lemma.lemmatize("better",pos="a"))
print(lemma.lemmatize("am",pos="v"))