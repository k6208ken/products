products = []
while True:
	name = input('請輸入商品名稱： ')
	if name == 'q':
		break
	price = input('請輸入商品價格： ')
	# p = [name,price]	
	products.append([name,price])
print(products)

for product in products:
	print('{}的價格是{}'.format(product[0],product[1]))
