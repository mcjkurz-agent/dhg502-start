import jieba

sentence = "我来到北京清华大学"
result = "/".join(jieba.cut(sentence))
print(result)
