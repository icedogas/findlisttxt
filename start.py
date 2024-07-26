def read_file(file_path):
    """Читает файл и возвращает список строк."""
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except Exception as e:
        print(f"Ошибка чтения файла {file_path}: {e}")
        return []


def write_file(file_path, data):
    """Записывает данные в файл."""
    try:
        with open(file_path, 'w') as file:
            for item in data:
                file.write(f"{item}\n")
    except Exception as e:
        print(f"Ошибка записи файла {file_path}: {e}")


def exclude_and_find_values(what, where):
    """Исключает значения из списка `what`, присутствующие в списке `where`,
     и возвращает два списка: оставшиеся и найденные значения."""
    remaining = [item for item in where if item not in what]
    found = [item for item in where if item in what]
    return remaining, found


def main():
    # Пути к файлам
    what_file = 'what.txt'
    where_file = 'where.txt'
    result_file = 'result.txt'
    find_file = 'found.txt'

    # Считывание значений из файлов
    what_list = read_file(what_file)
    where_list = read_file(where_file)

    # Исключение и нахождение значений
    result, found = exclude_and_find_values(what_list, where_list)

    # Сохранение результатов в файлы
    write_file(result_file, result)
    write_file(find_file, found)

    # Печать результатов
    print("Результат (оставшиеся значения):")
    for item in result:
        print(item)

    print("\nНайденные значения:")
    for item in found:
        print(item)


if __name__ == "__main__":
    main()
