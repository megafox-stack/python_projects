import numpy as ny
import sympy as sy
import matplotlib.pyplot as plt
print("\nSelect operation")
print("1 - Derivative")
print("2 - Integration")
print("3 - Limit")
print("4 - plot")
print("5 - talyor")
print("6 - exit")

choice = int(input("Enter choice: "))

while True:
        function = input("enter the function in terms of x:")
        try:
            eval(function,{"x":1,"ny":ny})
            break
        except:
            print("invalid function!try again")

def f(x):
    return eval(function,{"x":x,"ny":ny})

if choice == 1:

    order = int(input("enter the derivative order:(1,2,3):"))
    def derivative(f,x,h = 0.001):
        return (f(x+h) - f(x-h))/(2*h)

    x = sy.symbols('x')
    expr = sy.sympify(function)
    d = sy.diff(expr,x,order)

    x_val = float(input("enter the value of x:"))

    result = f
    for i in range(order):
         result = lambda x,g=result: derivative(g,x)



    print("approximate derivative:")
    sy.pprint(d)
    print("exact derivative:",d.subs(x,x_val))
    print("derivative value =",round(result(x_val),4))

elif choice == 2:
   
    a = float(input("enter the lower limit:"))
    b = float(input("enter the higher limit:"))

    n = 1000 #no of intervals

    x_val = ny.linspace(a,b,n)
    y_val = f(x_val)

    integral = ny.trapezoid(y_val,x_val)
    print("integral value:",integral)

elif choice == 3:
   
    x = sy.symbols('x')
    expr = sy.sympify(function)
    limit_point = float(input("enter the limit point:"))
    limit_value = sy.limit(expr,x,limit_point)
    print("limit = ",limit_value)


elif choice == 4:
     x_val = ny.linspace(-10,10,400)
     y_val = [eval(function) for x in x_val]
     plt.plot(x_val,y_val)
     plt.ylabel("x")
     plt.xlabel("y")
     plt.title("function graph")
     plt.show()

elif choice == 5:
   
    x = sy.symbols('x')
    expr = sy.sympify(function)

    point = float(input("expand around point: "))
    order = int(input("order of series: "))

    taylor = sy.series(expr, x, point, order)

    print("Taylor Series:")
    print(taylor)
      
else:
     print("exiting...")       

          



    