# 1
a = float(input("Enter a: "))
b = float(input("Enter b: "))
h = float(input("Enter h: "))
print("Area = %.2f" % ((a + b) * h / 2))

# 2
import math

r = float(input("Radius = "))
S = math.pi * r * r
P = 2 * math.pi * r
print("Area = %.3f\nPerimeter = %.3f" % (S, P))

# 3
hours = float(input("Enter hours: "))
rate = float(input("Enter rate: "))
print("Pay: %.2f" % (hours * rate))
