# 檢查檔案有沒有在作業系統裡面
import os # 作業系統with open('filename', 'r', encoding = 'utf-8') as f: # encoding是讀取文字			

# function只做一件事情
# 讀取檔案
def read_file(filename):
	products = [] # 產生空清單
	with open(filename, 'r', encoding = 'utf-8') as f:
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
	return products

# 讓使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break # 逃出迴圈
		price = input('請輸入商品價格: ')
		price = int(price)
		products.append([name, price]) # 將兩樣物品放入大清單
	print(products)
	return products

# 印出所有購買紀錄
def print_products(products):
	for p in products: # p 是名稱和價格
		print(p[0], '的價格是', p[1])

# 寫入檔案
def write_file(filename, products):
	with open('filename', 'w', encoding = 'utf-8') as f: # 寫入檔案W
		f.write('商品,價格\n') # \n是換行符號
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')


def main(): # main 是主要的執行程式
	filename = 'products.csv'
	if os.path.isfile(filename): # 檢查檔案在不在
		print('yeah! 找到檔案了!')
		products = read_file(filename)
	else:
		print('找不到檔案......')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()

# refactor 重構
