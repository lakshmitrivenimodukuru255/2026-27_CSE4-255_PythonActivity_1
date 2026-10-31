## Problem Statement
Write a Python program to automate stock reconciliation across multiple supply chain locations. The program must:

Loop through a list of locations.

Accept user inputs for quantities received, distributed, damaged, and the actual physical stock remaining.

Calculate the expected remaining stock using the formula: Received - Distributed - Damaged.

Identify any discrepancy (loss or mismatch) between expected and actual stock.

Calculate replenishment requirements if the actual stock falls below a predefined target stock level (100).


## Algorithm
1.Start and initialize locations list and target_stock = 100.

2.For each location in locations:

Print the location header.

Input received, distributed, damaged, and actual_remaining quantities.

Compute expected_remaining = received - distributed - damaged.

Compute discrepancy = expected_remaining - actual_remaining.

Compute replenishment = target_stock - actual_remaining (if actual_remaining < target_stock, else 0).

Print the expected remaining stock, discrepancy, and replenishment needed.

3.End.

## Python source code
```
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
    replenishment = (target_stock - actual_remaining if actual_remaining < target_stock else 0)
      
    print(f"-> Expected Remaining: {expected_remaining}")
    print(f"-> Discrepancy (Loss/Mismatch): {discrepancy}")
    print(f"-> Replenishment Needed: {replenishment}")
```

## Sample Input & Output
Sample Input:

Enter quantity received: 150
Enter quantity distributed: 80
Enter quantity damaged: 5
Enter physical stock remaining count: 60

Enter quantity received: 200
Enter quantity distributed: 120
Enter quantity damaged: 10
Enter physical stock remaining count: 70


Sample Output:
-> Expected Remaining: 65
-> Discrepancy (Loss/Mismatch): 5
-> Replenishment Needed: 40

--- Location 2 ---
-> Expected Remaining: 70
-> Discrepancy (Loss/Mismatch): 0
-> Replenishment Needed: 30

## Flowchart
```mermaid
graph TD
    Start([Start]) --> Init[locations = ['Location 1', 'Location 2'], target_stock = 100]
    Init --> Loop{For each location}
    
    Loop --> Input[Input received, distributed, damaged, actual_remaining]
    Input --> Calc[expected = received - distributed - damaged<br/>discrepancy = expected - actual<br/>replenishment = target - actual if actual < target else 0]
    Calc --> Print[Print expected, discrepancy, and replenishment]
    
    Print --> CheckMore{More locations?}
    CheckMore -- Yes --> Loop
    CheckMore -- No --> End([End])
```

