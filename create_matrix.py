import numpy
import add_Number

def create_matrix():
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))

    matrix = []

    #matrix = [[0 for _ in range(columns)] for _ in range(rows)]
    #print(matrix)

    print("Enter the numbers of the matrix")
    
    for i in range(rows):
        numbers = add_Number.add_number()
        if len(numbers) == columns:
            matrix.append(numbers)
        else:
            print("Se ingreso columnas demás en la matriz")
    '''
    for i in range(rows):
        for j in range(columns):
            print(i, j)
            number_str = str(input(f"Row {i + 1}, Column {j + 1}: "))
            number = complex(number_str)
            matrix[i][j] = number'''
    
    print(matrix)
    
    return matrix

matrix = create_matrix()
