# 問題2-7: 折り紙の貼り合わせ

sheets, height = 3,4
data = [2,1]
width = height

for i in range(sheets-1):
    overlap = data[i]
    width += height - overlap
    
area = height * width
print(area)