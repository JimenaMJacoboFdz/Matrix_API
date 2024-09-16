# Tuple representing a complex number (real part, imaginary part)
rectangular_tuple = (3, 4)

# Convert the tuple to a complex number
complex_number = complex(rectangular_tuple[0], rectangular_tuple[1])

# Print the complex number
print(f"Complex number: {complex_number}")

import cmath

# Define a complex number in rectangular form (a + bi)
rectangular_num = 3 + 4j  # Example: a = 3, b = 4

# Convert to polar form using cmath.polar()
r, theta = cmath.polar(complex_number)

# Print the results
print(f"Magnitude (r) = {r}")
print(f"Angle (theta, in radians) = {theta}")
print(f"Angle (theta, in degrees) = {cmath.phase(rectangular_num) * (180 / cmath.pi)}")