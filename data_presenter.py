open_file = open('Cupcakeinvoices.csv')

# for line in open_file:
#     print(line)

# for type in open_file:
#     type = (type.split(','))
#     print(type[2])
    

total = []

for type in open_file:
    type = (type.split(','))
    amt = int(type[3])
    price = float(type[4])
    invoices = amt * price
    total.append(invoices)
    print(amt * price)

print(f'Total Amt: {sum(total)}')



