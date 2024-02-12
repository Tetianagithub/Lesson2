a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
c = int(input("enter the third number: "))
operation = input("Enter '1', '2', or '3', where 1 = maxvalue, 2 = minvalue, 3 = averagevalue: ")

if operation == '1' and b <= a >= c:
    print(a)
elif operation == '1' and a <= b >= c:
    print(b)
elif operation == '1' and a <= c >= b:
    print(c)
if operation == '2' and b >= a <= c:
    print(a)
elif operation == '2' and a >= b <= c:
    print(b)
elif operation == '2' and a >= c <= b:
    print(c)
if operation == '3':
    result = (a + b + c)/3
    print("average", result)
else:
    print("Invalid operation. Please enter '1', '2', or '3', where 1 = maxvalue, 2 = minvalue, 3 = averagevalue.")
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