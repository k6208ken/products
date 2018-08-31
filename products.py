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

with open('products.csv','w',encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')	


