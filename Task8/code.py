stock = 10
price = 50
total_sales = 0
while True:
  print("\nStock left:", stock)
  ans = input("Order burger? (y/n): ")

  if ans != "y":
    break
  qty = int(input("Enter quantity: "))

  if qty <= stock:
    bill = qty * price
    stock -= qty
    total_sales += bill
    print("Success! Bill: ₹", bill)
  else:
    print("Rejected! Not enough stock.")
print("Total Sales: ₹", total_sales)
print("Remaining Stock:", stock)
