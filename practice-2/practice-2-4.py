# 問題2-4: \nは改行記号なので，3つの文が3行に渡って書かれていることになります．
# この文章中の単語を用いて，キーとして単語，値として出現数を持つような辞書word2freqを作成し，出力してください．ただし，改行記号は単語に含めないでください．
# ヒント：改行記号でsplitしてから空白でsplitすれば，単語に分割できます．
# 期待する出力：{'i': 2, 'bought': 1, 'an': 1, 'apple': 1, '.': 3, 'ate': 1, 'it': 2, 'is': 1, 'delicious': 1}
doc = 'i bought an apple .\ni ate it .\nit is delicious .'
word2freq = {}

lines = doc.split("\n")
for line in lines:
    word_separate_space = line.split()
    for word in word_separate_space:
        word2freq[word] = word2freq.get(word, 0) + 1

print(word2freq)