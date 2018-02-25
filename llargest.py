x=raw_input("enter the value of x = ")
y=raw_input("enter the value of y = ")
z=raw_input("enter the value of z = ")
if (int(x)>int(y) and int(z)<int(x)):
    print('x is greater')
elif (int(y)>int(x) and int(z)<int(y)):
    print('y is greater')
else:
    print('z is greater')