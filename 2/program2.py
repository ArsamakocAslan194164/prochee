import numpy as np
import random
import tempfile
import subprocess

# Адаптер вызова программы П1
def add_matrices(file_name1, file_name2, output_file):
    subprocess.run(['python', 'program1.py', file_name1, file_name2, output_file])

# Функция для генерации матриц и записи их в файл
def generate_matrices(file_name):
    n = random.randint(2, 5)
    m = random.randint(2, 5)
    data1 = np.random.random((n, m))
    data2 = np.random.random((n, m))
    with open(file_name, 'w') as f:
        for row1, row2 in zip(data1, data2):
            f.write(' '.join(str(x) for x in row1) + '\n')
            f.write(' '.join(str(x) for x in row2) + '\n')

# Генерация данных матриц и их сложение с помощью адаптера
def test_add_matrices():
    with tempfile.NamedTemporaryFile() as f1, tempfile.NamedTemporaryFile() as f2, tempfile.NamedTemporaryFile() as f3:
        generate_matrices(f1.name)
        generate_matrices(f2.name)
        add_matrices(f1.name, f2.name, f3.name)

        # Сравнение результата с ожидаемым значением
        a = np.genfromtxt(f1.name)
        b = np.genfromtxt(f2.name)
        expected = a + b
        result = np.genfromtxt(f3.name)
        assert np.allclose(result, expected)

# Запуск тестов
if __name__ == '__main__':
    test_add_matrices()