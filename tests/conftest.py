import logging

# Форматирование логов
LOG_FORMAT = '%(asctime)s [%(levelname)-5s] (%(filename)s:%(lineno)d) - %(message)s'

# Создание экземпляра FileHandler для записи в файл с кодировкой UTF-8
file_handler = logging.FileHandler(filename='tests.log', mode='w', encoding='utf-8')
file_handler.setFormatter(logging.Formatter(LOG_FORMAT))
file_handler.setLevel(logging.INFO)

# Фильтрация логов, показывающих только события из пакета tests.*
class TestsFilter(logging.Filter):
    def filter(self, record):
        return record.name.startswith('tests.')

# Обработчик логов для терминала
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter(LOG_FORMAT)
console_handler.setFormatter(formatter)

# Приложение фильтра к консольному обработчику
console_handler.addFilter(TestsFilter())

# Основной логгер
root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)

# Добавление обоих обработчиков (файл и терминал)
root_logger.addHandler(file_handler)
root_logger.addHandler(console_handler)