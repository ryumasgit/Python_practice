#問題4-8: ダイエットの連続記録
def weight_comparison(standard, weight, continue_count, max_continue_count, lazy_count, max_lazy_count):
    if weight > standard:
        max_continue_count = max(max_continue_count, continue_count)
        continue_count = 0
        lazy_count += 1
    elif weight < standard:
        max_lazy_count = max(max_lazy_count, lazy_count)
        lazy_count = 0
        continue_count += 1
        
    return continue_count, max_continue_count, lazy_count, max_lazy_count

executions = 8
input_data = [55,56,57,55,56,53,52,50]
standard = None
lazy_count = 0
max_lazy_count = 0
continue_count = 0
max_continue_count = 0

for i in range(executions):
    weight = input_data[i]
    if standard is None:
        standard = weight
    continue_count, max_continue_count, lazy_count, max_lazy_count = weight_comparison(
        standard, weight, continue_count, max_continue_count, lazy_count, max_lazy_count)
    standard = weight

max_continue_count = max(max_continue_count, continue_count)
max_lazy_count = max(max_lazy_count, lazy_count)
        
print(max_continue_count, max_lazy_count)