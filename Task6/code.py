print(" Smart Hostel Resource Monitoring ")
ELEC_RATE = 6.5  
WATER_RATE = 4.0  
ELEC_LIMIT = 150  
WATER_LIMIT = 300  
num_rooms = int(input("Enter number of rooms to monitor: "))
grand_total_cost = 0

for room in range(1, num_rooms + 1):
  print(f"\n-- Room {room} --")
  elec = float(input("Enter electricity consumption (kWh): "))
  water = float(input("Enter water consumption (units): "))

  elec_cost = elec * ELEC_RATE
  water_cost = water * WATER_RATE
  total_room_cost = elec_cost + water_cost
  grand_total_cost += total_room_cost

  print(f"Electricity Bill: ₹{elec_cost:.2f}")
  print(f"Water Bill: ₹{water_cost:.2f}")
  print(f"Total Room Bill: ₹{total_room_cost:.2f}")

  if elec > ELEC_LIMIT or water > WATER_LIMIT:
    print("ALERT: Consumption exceeds threshold limits!")
  else:
    print("Status: Within normal limits.")
print()
print(f"Total Utility Cost for Hostel: ₹{grand_total_cost:.2f}")
