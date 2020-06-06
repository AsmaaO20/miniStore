products = {
  'product1' : 200,
  'product2' : 150,
  'product3' : 300,
  'product4' : 50,
  'product5' :75
}

total = 0

##print('Please enter the info below.')
name = input('Your name...')
age = input('Your age...')
gender = input('Female(f) or Mele(m)...')
tel = input('Your number phone...')

if(int(age) < 18) : 
  print(f'Sorry {name}. you need to be above 18 years old. Come back when you older :D ')
else :
  print(f'Welcome {name} with us')
  
print('You can see below the products that we have:')
#list(products.keys()).index(product) for index of the dict

qst = 'y'

while(qst == 'y') :
  print('  products|Prices')
  for product in products :
    print(  product , products[product])
  name_item = input('Please enter name of the item that you want to buy .')

  #if the user enter the name with cap
  name_item = name_item.lower()

  if(name_item not in products ) :
    print('We don\'t have this item')
  else :
    print(f'This item {name_item} cost :')
    cost = products.get(name_item)
    total = int(total) + int(cost)
    print(products.get(name_item))


  qst = input('type (y) if you want to buy other item ')

money_have = input(f'you have {total} please enter the money to buy')

the_rest_of_the_bill = int(money_have) - total

print(f'Here is your rest of the bill {the_rest_of_the_bill}\nThank you {name} hope to see you again ')