import sys
import os


# Определение алгоритмов сортировки
def selection_sort(arr):  # Сортировка выбором
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr):  # Сортировка вставками
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):  # Сортировка слиянием
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


# Определение имени входных и выходных файлов
if len(sys.argv) < 2:
    print("Необходимо указать тип сортировки (selection, insertion или merge)")
    sys.exit()

alg = sys.argv[1]  # Алгоритм сортировки
input_file = sys.argv[2]  # Входной файл с данными
output_file = sys.argv[3]  # Выходной файл с результатами

# Проверка наличия файлов и правильности указания их имён
if not os.path.isfile(input_file):
    print("Файл с входными данными не найден")
    sys.exit()

if not os.path.isfile(output_file):
    print("Файл с выходными данными не найден")
    sys.exit()

# Чтение данных из входного файла и проверка на корректность
try:
    with open(input_file, 'r') as f:
        data = f.readlines()
        data = [int(x.strip()) for x in data]
except (ValueError, IOError):
    print("Ошибка чтения входных данных")
    sys.exit()

# Проверка корректности алгоритма сортировки, переданного в качестве параметра
if alg not in ['selection', 'insertion', 'merge']:
    print("Некорректный тип сортировки")
    sys.exit()

# Выбор алгоритма сортировки и сортировка данных
if alg == 'selection':
    sorted_data = selection_sort(data)
elif alg == 'insertion':
    sorted_data = insertion_sort(data)
elif alg == 'merge':
    sorted_data = merge_sort(data)

# Запись отсортированных данных в выходной файл
try:
    with open(output_file, 'w') as f:
        for i in sorted_data:
            f.write(str(i) + "\n")
except IOError:
    print("Ошибка записи выходных данных")
    sys.exit()