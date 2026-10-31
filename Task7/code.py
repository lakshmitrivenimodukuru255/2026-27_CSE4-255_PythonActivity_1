balance = 5000
pin = input("Enter PIN (1234): ")
if pin == "1234":
  print("\n1. Check Balance")
  print("2. Deposit")
  print("3. Withdraw")
  choice = input("Choose option (1/2/3): ")

  if choice == "1":
    print(f"Current Balance: ₹{balance}")

  elif choice == "2":
    amount = float(input("Enter amount to deposit: ₹"))
    balance += amount
    print(f"Deposited successfully! New Balance: ₹{balance}")

  elif choice == "3":
    amount = float(input("Enter amount to withdraw: ₹"))
    if amount <= balance:
      balance -= amount
      print(f"Please collect cash. Remaining Balance: ₹{balance}")
    else:
      print("Error: Insufficient balance!")

  else:
    print("Error: Invalid option selected.")

else:
  print("Error: Incorrect PIN!")
