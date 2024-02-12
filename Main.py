meters = int(input("enter the number of meters: "))
operation = input("Enter 'miles', 'inches', или 'yards': ")
if operation == 'miles':
    result = (meters / 1609)
    print("miles:", result)
elif operation == 'inches':
    result = (meters * 39.37)
    print("inches:", result)
elif operation == 'yards':
    result = (meters * 1.094)
    print("yards:", result)
else:
    print("Invalid operation. Please enter 'miles', 'inches', or 'yards'.")