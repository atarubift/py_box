import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from janome.tokenizer import Tokenizer
from sklearn.feature_extraction.text import TfidfTransformer
import os
import csv

filenames = sorted(os.listdir(path='./text'))
print(filenames)
wakati_list = []
for filename in filenames:
  # print(filename)
  with open("./text/" + filename, mode='r', encoding="utf-8") as f:
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
  # print(wakati_list)
wakati_list_np = np.array(wakati_list)

vectorizer = TfidfVectorizer(token_pattern=u'\\b\\w+\\b')
transformer  = TfidfTransformer()
tf = vectorizer.fit_transform(wakati_list_np)
tfidf = transformer.fit_transform(tf)
tfidf_array = tfidf.toarray()
cs = cosine_similarity(tfidf_array, tfidf_array)
np.set_printoptions(threshold=1000)
with open('results.csv', 'wt') as f:
  writer = csv.writer(f)
  writer.writerows(cs)