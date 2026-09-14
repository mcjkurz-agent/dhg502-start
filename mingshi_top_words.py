from collections import Counter

import jieba

with open("明史.txt", encoding="utf-8") as f:
    text = f.read()

words = [w for w in jieba.cut(text) if w.strip() and len(w) > 1]
for word, count in Counter(words).most_common(10):
    print(word, count)
