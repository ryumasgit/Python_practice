# 問題5: ファイル操作とデータ処理
# テキストファイルからデータを読み取り、指定された条件に合致する行を抽出するプログラムを書いてください。例えば、特定の単語が含まれている行を抽出するなどの条件を指定できるようにしてください。
f = open('./python_practice/team-lab/myfile.txt', 'r')

data = f.read()
print(data)

f.close()