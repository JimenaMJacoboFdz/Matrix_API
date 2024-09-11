import numpy as np

#import add_Number
import create_matrix as matrix

if __name__ == "__main__":
    system = matrix.create_matrix()
    result = matrix.create_matrix()
    solution = np.linalg.solve(system, result)
    print(solution)