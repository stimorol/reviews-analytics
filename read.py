data = []
count = 0
text_count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了！總共有', len(data), '筆資料')
for text in data:
	text_count += len(text)
print('留言平均長度是', int(text_count / len(data)), '字')

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '則小於100字的留言')
print(new[10])