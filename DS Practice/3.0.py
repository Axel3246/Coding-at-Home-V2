#https://www.youtube.com/watch?v=gDqQf4Ekr2A&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=3&ab_channel=codebasics

stock_price = [298, 305, 320, 301, 292]

#What was the price on day 3

print(stock_price[2])

#On what day the price was 301

for i in range (len(stock_price)):  # O(n)
    if stock_price[i] == 301:
        print(i)

#Print everything

for i in stock_price:
    print(i)

#Add a value

stock_price.insert(1, 284)

#Delete a value

stock_price.remove(305)
#yeah