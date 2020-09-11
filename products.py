# 讀取檔案
products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if '商品,價格' in line: # 跳過這兩個字
			continue # continue是跳到下一回，只能寫在for loop裡面，且continue通常在迴圈中比較高的地方
		name, price = line.strip().split(',')
		# strip()來除掉換行符號(\n)
		# 用split(',')來用逗點做分割
		# 加上encoding = 'utf-8'來讀取
		# 解釋split完後會變成清單
		# 將讀到的內容裝入清單
		products.append([name, price]) # 將兩樣物品放入清單
print(products)

# 讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break # 逃出迴圈
	price = input('請輸入商品價格: ')
	price = int(price)
	products.append([name, price]) # 將兩樣物品放入大清單
print(products)

# 印出所有購買紀錄
for p in products: # p 是名稱和價格
	print(p, '的價格是', p[1])

# 寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f: # 寫入檔案W
	f.write('商品,價格\n') # \n是換行符號
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
		


