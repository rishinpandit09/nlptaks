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

texts = """Doctor Strange in the Multiverse of Madness is a 2022 American superhero film based on Marvel Comics featuring the character Doctor Strange. Produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures, it is the sequel to Doctor Strange (2016) and the 28th film in the Marvel Cinematic Universe (MCU). The film was directed by Sam Raimi, written by Michael Waldron, and stars Benedict Cumberbatch as Stephen Strange, alongside Elizabeth Olsen, Chiwetel Ejiofor, Benedict Wong, Xochitl Gomez, Michael Stuhlbarg, and Rachel McAdams. In the film, Strange protects America Chavez (Gomez), a teenager capable of traveling the multiverse, from Wanda Maximoff (Olsen).
Doctor Strange director and co-writer Scott Derrickson had plans for a sequel by October 2016. He signed to return as director in December 2018, when Cumberbatch was confirmed to return. The film's title was announced in July 2019 along with Olsen's involvement, while Jade Halley Bartlett was hired to write the film that October. Derrickson stepped down as director in January 2020, citing creative differences. Waldron and Raimi joined the following month and started over, adding elements of the horror genre that Raimi had worked with previously and making Maximoff the villain of the film, continuing her story from the series WandaVision (2021). Filming began in November 2020 in London but was put on hold in January 2021 due to the COVID-19 pandemic. Production resumed by March 2021 and concluded in mid-April in Somerset. Shooting also occurred in Surrey and Los Angeles.
Doctor Strange in the Multiverse of Madness premiered at the Dolby Theatre in Hollywood on May 2, 2022, and was released in the United States on May 6, as part of Phase Four of the MCU. The film received praise for Raimi's direction, the visuals, and Olsen's performance, while criticism was mostly directed towards the plot. The film has grossed $954 million worldwide, making it the second-highest-grossing film of 2022."""
for text in texts:
    sentences = nltk.sent_tokenize(texts)
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(words)
        print(tagged)
