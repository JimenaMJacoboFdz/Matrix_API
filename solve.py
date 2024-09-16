import cmath 

# Function to multiply two complex numbers
def complex_multiply(a, b):
    return (a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0])

# Function to subtract two complex numbers
def complex_subtract(a, b):
    return (a[0] - b[0], a[1] - b[1])

# Function to divide two complex numbers
def complex_divide(a, b):
    denom = b[0]**2 + b[1]**2
    return ((a[0]*b[0] + a[1]*b[1]) / denom, (a[1]*b[0] - a[0]*b[1]) / denom)

# Calculate determinant of a 2x2 matrix
def determinant(a11, a12, a21, a22):
    # a11 * a22 - a12 * a21 (complex multiplication and subtraction)
    return complex_subtract(complex_multiply(a11, a22), complex_multiply(a12, a21))


def determinant_polar(a11, a12, a21, a22):
    part1 = complex_multiply(a11, a22)
    part2 = complex_multiply(a12, a21)
    complex_num = complex_subtract(part1, part2)
    complex_tuple = complex(complex_num[0], complex_num[1])
    r, theta = cmath.polar(complex_tuple)
    print(f"Magnitude (r) = {r}")
    print(f"Angle (theta, in radians) = {theta}")
    return r, theta

# Coefficients of the matrix A (as tuples of real and imaginary parts)
a11 = (2, 3)  # 2 + 3i
a12 = (1, -1)  # 1 - i
a21 = (1, -2)  # 1 - 2i
a22 = (3, 1)  # 3 + i

# Constants (right-hand side)
b1 = (4, 2)  # 4 + 2i
b2 = (1, -1)  # 1 - i

# Determinant of matrix A
det_A = determinant(a11, a12, a21, a22)
det_A_p = determinant_polar(a11, a12, a21, a22)

# Determinants of modified matrices
# For z1: replace first column with B
det_A1 = determinant(b1, a12, b2, a22)
det_A1_p = determinant_polar(b1, a12, b2, a22)

# For z2: replace second column with B
det_A2 = determinant(a11, b1, a21, b2)
det_A2_p = determinant_polar(a11, b1, a21, b2)

# Solve for z1 and z2 using Cramer's rule
z1 = complex_divide(det_A1, det_A)
z2 = complex_divide(det_A2, det_A)
z1_p = det_A1_p[0]/det_A_p[0]
theta1 = (det_A1_p[1] - det_A_p[1])*180/cmath.pi
# Convert polar to rectangular form
#rectangular_num1 = cmath.rect(z1, theta1)
z2_p = det_A2_p[0]/det_A_p[0]
theta2 = (det_A2_p[1] - det_A_p[1])*180/cmath.pi
#rectangular_num2 = cmath.rect(z2, theta2)
#z2 = det_A2/det_A

print(det_A)
print(det_A1)
print(det_A2)
# Output the solutions
print(f"z1 = {z1_p} < {theta1}°")
print(f"z2 = {z1[0]} + {z1[1]}i")
#print(rectangular_num1)
print(f"z2 = {z2_p} < {theta2}°")
#print(rectangular_num2)
print(f"z2 = {z2[0]} + {z2[1]}i")
