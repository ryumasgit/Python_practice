# 問題8: 文字列操作
# 与えられた文字列内で特定の文字やサブ文字列の出現回数をカウントするプログラムを書いてください。

import re
# 入力テキスト
text = "Python is an easy-to-learn programming language. Python is widely used in web development and data analysis. Python is versatile and powerful."

# カウントする文字列
target_string = "Python"

# プログラムの実行
def string_count(target,text):
    m = re.findall(target, text)
    return len(m)

print(string_count(target_string, text))
# 出力:
# "Python" がテキスト内で 3 回出現します。
