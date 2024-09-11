import numpy
import add_Number

def create_matrix():
    print("")
    print("-----------------------------------------------------")
    rows = int(input("Enter the number of rows:          "))
    columns = int(input("Enter the number of columns:       "))
    print("-----------------------------------------------------")

    matrix = []

    while len(matrix) < rows:
        
        print(f"You are in the row:      {len(matrix)}")
        numbers = add_Number.add_number()
        if len(numbers) == columns:
            matrix.append(numbers)
        else:
            print("Se ingreso columnas demás en la matriz")

    print(matrix)
    
    return matrix
