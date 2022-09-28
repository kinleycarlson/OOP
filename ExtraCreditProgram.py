import ExtraCreditClass as ec


cust1 = ec.Customer('John','1234 Main Street','123-456-7890')
car1 = ec.Car('Hyundai','Venue','2021')
quote = ec.ServiceQuote(100,300)

print('Name:',cust1.get_name())
print('Address:',cust1.get_address())
print('Phone',cust1.get_phone())

print()

print('Make:',car1.get_make())
print('Model:',car1.get_model())
print('Year:',car1.get_year())

print()

quote.get_sales_tax()
print(sales_tax)