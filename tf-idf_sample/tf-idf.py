from sklearn.feature_extraction.text import TfidfVectorizer
from janome.tokenizer import Tokenizer
import pandas as pd

# TF-IDFを求めたい文書のリスト
docs = [
  '今日 学校 体育 授業 バレー トス レシーブ 授業 先生 クラブ バレー 放課後',
  '今日 放課後 クラブ 活動 サッカー 試合 サッカー 合宿 ゴール キーパー'
]

# モデルの生成
vectorizer = TfidfVectorizer(smooth_idf= False)

# TF-IDFの計算
values = vectorizer.fit_transform(docs).toarray()

# 特徴量ラベルの取得
words = vectorizer.get_feature_names()

# 結果
df = pd.DataFrame(values, columns = words)
print(df.T.sort_values(by=0,ascending=False)[0])
print('-------------')
print(df.T.sort_values(by=1,ascending=False)[1])