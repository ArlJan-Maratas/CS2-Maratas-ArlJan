# Electricity Bill Calculator
RATE = 12.90

while True:
    name = input("Enter customer name: ")
    
    if name.strip() != "":
        break
    else:
        print("Invalid. Please input a name.")
    
while True:
    previous = float(input("Enter previous meter reading: "))
    
    if previous >= 0:
        break 
    else:
        print("Invalid. Please input the previous meter reading which must be atleast 0.")
        
while True:
    current = float(input("Enter current meter reading: "))
    
    if current > previous:
        break 
    else:
        print("Invalid. Please input a current meter reading equal to or more than the previous reading.")

consumption = current - previous
total_bill = consumption * RATE
 
print("Electricity Consumption:", consumption, "kWh")   
print("Total Bill: PHP", round(total_bill, 2))

# Validation rules
# 1. Customer name -- Must not be empty
# 2. Previous reading -- Number at least 0
# 3. Current reading -- Number at least the previous reading