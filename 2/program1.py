import numpy as np

# Функция для сложения матриц
def matrix_sum(a, b):
    return a + b

# Чтение данных из файла
def read_data(file_name):
    with open(file_name, 'r') as f:
        data = []
        for line in f:
            row = [float(x) for x in line.strip().split()]
            data.append(row)
        return np.array(data)

# Запись данных в файл
def write_data(file_name, data):
    with open(file_name, 'w') as f:
        for row in data:
            f.write(' '.join(str(x) for x in row) + '\n')

# Функция для вызова из других программ
def add_matrices(file_name1, file_name2, output_file):
    # Чтение матриц из файлов
    a = read_data(file_name1)
    b = read_data(file_name2)

    # Сложение матриц
    result = matrix_sum(a, b)

    # Сохранение результата в файл
    write_data(output_file, result)