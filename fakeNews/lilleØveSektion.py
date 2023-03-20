import pandas as pd
from gensim.models import Word2Vec

def check(inp):
    if inp in model.wv.key_to_index:
        return model.wv[inp]
    else:
        return None

df = pd.read_csv('redactedNews.csv')
print(df["content"])
print(df.at[2, "content"])

df['content'] = df['content'].apply(lambda x: x.split())
model = Word2Vec(df['content'], vector_size=50, window=5, min_count=5, workers=4)
df['content'] = df['content'].apply(lambda x: [check(word) for word in x])
print(df)
print(df["content"])
print(df.at[2, "content"])