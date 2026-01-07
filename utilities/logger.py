import logging

# Создаем базовую конфигурацию логгера
LOG_FORMAT = '%(asctime)s [%(levelname)-5s] (%(filename)s:%(lineno)d) - %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

logger = logging.getLogger(__name__)