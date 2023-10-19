# 問題15: ピタゴラスの定理
# 与えられた整数の中から、ピタゴラスの定理 (a^2 + b^2 = c^2) を満たす整数の組み合わせを見つけるプログラムを書いてください。たとえば、a, b, c の値を見つけるプログラムとして実装します。


nums1 = (3, 4, 5)
nums2 = (5, 12, 13)
nums3 = (6, 8, 10)
nums4 = (7, 24, 25)

def is_pythagorean_theorem(nums):
    a_squared = nums[0] ** 2
    b_squared = nums[1] ** 2
    c_squared = nums[2] ** 2

    if a_squared + b_squared == c_squared:
        return True
    else:
        return False

results = []
for nums in [nums1,nums2,nums3,nums4]:
    results.append(is_pythagorean_theorem(nums))

for i, result in enumerate(results, 1):
    if result:
        print(f"組み合わせ {i}: ピタゴラスの定理を満たします.")
    else:
        print(f"組み合わせ {i}: ピタゴラスの定理を満たしません.")