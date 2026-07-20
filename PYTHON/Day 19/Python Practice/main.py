import calculator

print("Arithmetic Operations:")
print("Addition:", calculator.arithmetic.add(10, 5))
print("Subtraction:", calculator.arithmetic.sub(10, 5))
print("Multiplication:", calculator.arithmetic.mul(10, 5))
print("Division:", calculator.arithmetic.div(10, 5))

print("Advanced Operations:")
print("Power:", calculator.advanced.power(10, 2))
print("Perimeter:", calculator.advanced.perimeter(10, 5))
print("Area:", calculator.advanced.area(10, 5))
print("Circle Area:", calculator.advanced.circle_area(10))
print("Circle Circumference:", calculator.advanced.circle_circumference(10))

print("Converter Operations:")
print("INR to USD:", calculator.converter.inr_to_usd(10))
print("USD to INR:", calculator.converter.usd_to_inr(10))
print("Celsius to Fahrenheit:", calculator.converter.celsius_to_fahrenheit(10))
print("Fahrenheit to Celsius:", calculator.converter.fahrenheit_to_celsius(10))

