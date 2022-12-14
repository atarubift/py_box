import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from janome.tokenizer import Tokenizer
from sklearn.feature_extraction.text import TfidfTransformer

filenames = ['text1.txt', 'text2.txt', 'text3.txt', 'text4.txt', 'text5.txt']
wakati_list = []
for filename in filenames:
  with open(filename, mode='r', encoding="utf-8") as f:
    text = f.read()
  wakati = ''
  t = Tokenizer()
  for token in t.tokenize(text):
    hinshi = (token.part_of_speech).split(',')[0]
    hinshi_2 = (token.part_of_speech).split(',')[1]
    if hinshi in ['名詞']:
      if not hinshi_2 in ['空白', '*']:
        word = str(token).split()[0]
        if not ',*,' in word:
          wakati  = wakati + word + ' '
  wakati_list.append(wakati)
wakati_list_np = np.array(wakati_list)

vectorizer = CountVectorizer(token_pattern=u'\\b\\w+\\b')
transformer = TfidfTransformer()
tf = vectorizer.fit_transform(wakati_list_np)
tfidf = transformer.fit_transform(tf)
tfidf_array = tfidf.toarray()
cs = cosine_similarity(tfidf_array,tfidf_array)
print(cs)