# 問題12: マルチスレッドプログラミング
# マルチスレッドを使用して、複数のスレッドが同時に動作するプログラムを書いてください。例えば、複数のスレッドが並列で数値計算を実行するなどのシナリオを含めます。
#これらの問題は、プログラミングスキルの向上に挑戦的な要素を提供します。問題ごとに異なるスキルとアルゴリズムが必要とされ、幅広いプログラミング領域をカバーしています。問題を解く際に、効率的なアルゴリズムやベストプラクティスを考慮することが大切です。

import threading
import math

lists = [1, 4, 9, 16, 25]

def calculation_sqrt(number):
    return math.sqrt(number)

if __name__ == "__main__":
    threads = []
    results = []

    for number in lists:
        thread = threading.Thread(target=lambda num=number: results.append(calculation_sqrt(num)))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print("元のリスト:", lists)
    print("更新後のリスト:", results)
