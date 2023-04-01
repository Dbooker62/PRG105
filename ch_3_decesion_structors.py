print('play prices per ticket')
print('\n1. student $5.00')
print('\n2. veteran $7.00')
print('\n3. show sponser $2.00')
print('\n4. retired $6.00')
print('\n5. general public $10.00')
category=int( input('\n please enter the number of the category you fit for purchasing tickets:  '))
total_tickets=int(input('\n how many tickets would you like to buy?'  ))


if category == 1 :
    ticket_price = 5.00
elif category == 2:
    ticket_price = 7.00
elif category == 3:
    ticket_price = 2.00
elif category == 4:
    ticket_price = 6.00
elif category == 5:
    ticket_price = 10.00
else:
    print('invalid category entered')



if total_tickets >= 4 and total_tickets <= 8:
    discount = 0.10
elif total_tickets >= 9 and total_tickets <= 15:
    discount = 0.15
elif total_tickets > 15:
    discount = 0.20
else:
    discount = 0.00


subtotal =total_tickets * ticket_price
discounted_price = subtotal * discount
total = subtotal - discounted_price


print('cost before any discount were applied: $', subtotal)
print('your cost after are discounts were applied: $',total)
print('your price is $',round(ticket_price-(ticket_price * discount),2),' per ticket')


