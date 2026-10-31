locations = ["Location 1", "Location 2"]
target_stock = 100  

for i in locations:
  print(f"\n--- {i} ---")
  received = int(input("Enter quantity received: "))
  distributed = int(input("Enter quantity distributed: "))
  damaged = int(input("Enter quantity damaged: "))
  actual_remaining = int(input("Enter physical stock remaining count: "))
  
  expected_remaining = received - distributed - damaged
  discrepancy = expected_remaining - actual_remaining
  replenishment = (target_stock - actual_remaining if actual_remaining < target_stock else 0 )
  
  print(f"-> Expected Remaining: {expected_remaining}")
  print(f"-> Discrepancy (Loss/Mismatch): {discrepancy}")
  print(f"-> Replenishment Needed: {replenishment}")
