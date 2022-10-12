# import TextBlob
from textblob import TextBlob

my_sentence = TextBlob("Helllo Twitter, thist is Samuel_py do followw for Python tipps")

# using TextBlob.correct()
my_sentence = my_sentence.correct()

print(my_sentence)
