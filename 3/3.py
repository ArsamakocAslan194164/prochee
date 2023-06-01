import sys

class MatrixOperation:

    def __init__(self, filename):
        self.filename = filename
        self.matrix = []

    def read_file(self):
        with open(self.filename, 'r') as file:
            lines = file.readlines()
            self.matrix = [[int(num) for num in line.split()] for line in lines]

    def write_file(self, output_filename):
        with open(output_filename, 'w') as file:
            for row in self.matrix:
                file.write(' '.join(str(num) for num in row) + '\n')

    def perform_operation(self):
        pass


class TransposeMatrix(MatrixOperation):

    def __init__(self, filename):
        super().__init__(filename)

    def perform_operation(self):
        self.read_file()
        n = len(self.matrix)
        m = len(self.matrix[0])
        transposed = []
        for j in range(m):
            row = []
            for i in range(n):
                row.append(self.matrix[i][j])
            transposed.append(row)
        self.matrix = transposed


class AddMatrices(MatrixOperation):

    def __init__(self, filename1, filename2):
        super().__init__(filename1)
        self.filename2 = filename2

    def perform_operation(self):
        self.read_file()
        with open(self.filename2, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                row = [int(num) for num in line.split()]
                for j, val in enumerate(row):
                    self.matrix[i][j] += val


class FindDeterminant(MatrixOperation):

    def __init__(self, filename):
        super().__init__(filename)

    def perform_operation(self):
        self.read_file()
        n = len(self.matrix)
        if n == 1:
            self.matrix = self.matrix[0][0]
        elif n == 2:
            self.matrix = self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
        else:
            det = 0
            for j in range(n):
                sign = (-1) ** j
                sub_matrix = []
                for i in range(1, n):
                    row = []
                    for k in range(n):
                        if k != j:
                            row.append(self.matrix[i][k])
                    sub_matrix.append(row)
                sub_det = FindDeterminant('sub_matrix.txt')
                sub_det.matrix = sub_matrix
                sub_det.perform_operation()
                det += sign * self.matrix[0][j] * sub_det.matrix
            self.matrix = det


if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    operation = sys.argv[3]

    if operation == 'transpose':
        matrix_op = TransposeMatrix(input_file)
        matrix_op.perform_operation()
        matrix_op.write_file(output_file)
    elif operation == 'add':
        input_file2 = sys.argv[4]
        matrix_op = AddMatrices(input_file, input_file2)
        matrix_op.perform_operation()
        matrix_op.write_file(output_file)
    elif operation == 'det':
        matrix_op = FindDeterminant(input_file)
        matrix_op.perform_operation()
        with open(output_file, 'w') as file:
            file.write(str(matrix_op.matrix))
    else:
        print('Invalid operation')
        sys.exit(1)
