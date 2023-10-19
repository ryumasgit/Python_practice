# 問題5: ファイル操作とデータ処理
# テキストファイルからデータを読み取り、指定された条件に合致する行を抽出するプログラムを書いてください。例えば、特定の単語が含まれている行を抽出するなどの条件を指定できるようにしてください。
def extract_target_line(target):
    if target >= 1 and target < 4:
        with open('./python_practice/team-lab/myfile.txt', 'r') as f:
            lines = f.read().splitlines()
            target_line = lines[target - 1]
        print(target_line)
    else:
        print("1~3で指定して下さい")

extract_target_line(3)