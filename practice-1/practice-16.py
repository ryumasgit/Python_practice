# 問題16: 確率統計
# サイコロをN回振った結果（1から6までの目の出現回数）が記録されたデータが与えられます。このデータを元に、各目が出る確率を計算するプログラムを作成してください。具体的には、各目が出る確率をパーセンテージとして表示する関数を実装してください。

dice_data = [15, 20, 12, 18, 25, 10]

def calculation_dice_probabilities(target):
    data_total = sum(target)

    for i in range(1,7):
        percent = (target[i-1] / data_total) * 100
        print(f"サイコロの{i}の目が出る確率は、{percent:.2f}%です。")

calculation_dice_probabilities(dice_data)