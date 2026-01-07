import os
import sys
import pytest

def run_pytest():
    """
    Функция запускает pytest и возвращает статус завершения.
    """
    # Определим рабочий каталог, в котором располагается исполняемая программа
    base_dir = getattr(sys, '_MEIPASS', '.')  # Получаем базовый путь исполняемого файла
    tests_dir = os.path.join(base_dir, 'tests')  # Формируем путь к директории с тестами

    args = [tests_dir]
    exit_code = pytest.main(args)
    return exit_code

if __name__ == '__main__':
    sys.exit(run_pytest())