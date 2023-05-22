# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру
# строки и столбца. Аргументы num_rows и num_columns указывают число строк и
# столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов
# идет с единицы

def print_operation_table(operation, num_rows=6, num_columns=6):
    for x in range(1, num_rows+1):
        print(" ".join([str(operation(x, y)) for y in range(1, num_columns+1)]))


print(print_operation_table(lambda x, y: x * y))

# почему в конце добавляет None не понял
