room_capacity = 2
room_occupants = []
assigned_ids = set()
unallocated = 0
students = [("S1", "Rupa"), ("S2", "Nitya"), ("S1", "Rupa"), ("S3", "Nandu")]

for id, name in students:
  if id in assigned_ids:
    print(f"Duplicate: {name} is already assigned.")
  elif len(room_occupants) < room_capacity:
    room_occupants.append(name)
    assigned_ids.add(id)
    print(f"Allocated {name} successfully.")
  else:
    print(f"Room is full! {name} unallocated.")
    unallocated += 1
print("Room Occupants:", room_occupants)
print("Unallocated Demand:", unallocated)
