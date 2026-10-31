## Problem Statement
Write a Python program to simulate a basic ATM transaction sequence. The program must:
PIN Authentication: Prompt the user to enter a 4-digit PIN ("1234"). If incorrect, deny access with an error message.
Menu Options: If authenticated successfully, display a menu with three choices:

Check Balance

Deposit Money

Withdraw Money
Transaction Handling:

Option 1: Display the current account balance.

Option 2: Accept a deposit amount, add it to the balance, and display the new balance.

Option 3: Accept a withdrawal amount, check if the amount is less than or equal to the available balance, deduct it, and display the remaining balance (or show an insufficient funds error).

Error Handling: Handle invalid menu selections gracefully.



## Algorithm
1.Start the program and initialize balance = 5000.

2.Prompt the user to input their pin.

3.Check if pin == "1234":

4.If True:&ebsp;
Display the ATM menu (1. Check Balance, 2. Deposit, 3. Withdraw).

5.Prompt the user for a choice.

6.If choice == "1": Print the current balance.

7.Else if choice == "2": Input deposit amount, add to balance, and print the updated balance.

8.Else if choice == "3": Input withdrawal amount. Check if amount <= balance:

9.If true, subtract from balance and print success with remaining balance.

10.If false, print an insufficient balance error.

11.Else: Print an invalid option error.

12.If False (Incorrect PIN): Print an incorrect PIN error message.

13.End the program.

## Python source code
```
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
```
## Sample input & output

Sample input:

Enter PIN (1234): 1234
Choose option (1/2/3): 1

Sample output:

1. Check Balance
2. Deposit
3. Withdraw
Current Balance: ₹5000

## Flowchart
``` mermaid
graph TD
    A[Start: Initialize balance = 5000] --> B[Input PIN]
    B --> C{PIN == "1234"?}
    C -- No --> D[Print Error: Incorrect PIN] --> E[End]
    C -- Yes --> F[Display ATM Menu & Input choice]
    F --> G{choice == "1"?}
    G -- Yes --> H[Print Current Balance] --> E
    G -- No --> I{choice == "2"?}
    I -- Yes --> J[Input Deposit Amount & Add to Balance] --> K[Print New Balance] --> E
    I -- No --> L{choice == "3"?}
    L -- Yes --> M[Input Withdrawal Amount]
    M --> N{Amount <= Balance?}
    N -- Yes --> O[Deduct Amount & Print Remaining Balance] --> E
    N -- No --> P[Print Error: Insufficient Balance] --> E
    L -- No --> Q[Print Error: Invalid Option Selected] --> E
```
