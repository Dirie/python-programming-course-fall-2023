sno = [1,2,3,4,5]
item = ["iphone 14","iphone x max","iphone 14","iphone 12","iphone 11 p m", ]
quantity = [12,3,4,5,2]
price = [1200,1100,450,300,200]
amount = []
print('sno\titem name\t\tquantity\tprice\tamount')
for i in range(0,len(sno)):
    print(str(sno[i]) + '\t' + item[i] + '\t\t' + str(quantity[i]) + '\t\t' + str(price[i]) + '\t' + str(quantity[i] * price[i]))