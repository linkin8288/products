# two dimentional list
# 大清單裡面有小清單

products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break # 逃出迴圈
	price = input('請輸入商品價格: ')
	products.append([name, price]) # 將兩樣物品放入大清單
print(products)

for p in products: # p 是名稱和價格
	print(p)



