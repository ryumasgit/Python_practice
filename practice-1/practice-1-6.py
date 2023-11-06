# 問題6: 複雑な規則性のパターン検出
# 与えられたデータセットに含まれる複雑な規則性を見つけ、そのパターンに従ったデータ処理プログラムを書いてください。
# これらの問題は、基本的なプログラミングスキルからより高度なスキルまで幅広い要素をカバーしています。それぞれの問題を解くことで、プログラミングの能力とコーディングスキルを向上させるのに役立つでしょう。また、関連するテクニカルリソースやプログラミング言語の文法を確認することも忘れないでください。

import re

def extract_email(target):
    print(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+', target))

text = "This is a sample text with email addresses example@email.com and contact@example.com. Please contact us at info@example.org."
extract_email(text)