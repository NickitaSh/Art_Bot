import os
# импортируем модуль emoji для отображения эмоджи
from emoji import emojize

# токен выдаётся при регистрации приложения
TOKEN = ''
# название БД
NAME_DB = 'products.sqlite'
# версия приложения
VERSION = '0.0.1'
AUTHOR = 'User'

# родительская директория
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# путь до базы данных
DATABASE = os.path.join('sqlite:///' + BASE_DIR, NAME_DB)

COUNT = 0

# кнопки управления
KEYBOARD = {
    'CHOOSE_GOODS': emojize(':open_file_folder: Выбрать товар'),
    'INFO': emojize(':speech_balloon: О магазине'),
    'SETTINGS': emojize('U+2699'),
    'SEMIPRODUCT': emojize(':pizza: Полуфабрикаты'),
    'GROCERY': emojize(':bread: Бакалея'),
    'ICE_CREAM': emojize(':shaved_ice: Мороженое'),
    '<<': emojize(':fast reverse button:'),
    '>>': emojize(':fast-forward button:'),
    'BACK_STEP': emojize(':arrow_left:'),
    'NEXT_STEP': emojize(':arrow_right:'),
    'ORDER': emojize(':check mark button: Заказ:'),
    'X': emojize(':cross mark:'),
    'DOUWN': emojize(':downwards button:'),
    'AMOUNT_PRODUCT': COUNT,
    'AMOUNT_ORDERS': COUNT,
    'UP': emojize(':upwards button:'),
    'APPLAY': emojize(':check mark button: Оформить заказ'),
    'COPY': emojize(':copyright:')
}

# id категорий продуктов
CATEGORY = {
    'SEMIPRODUCT': 1,
    'GROCERY': 2,
    'ICE_CREAM': 3,
}

# название команд
COMMANDS = {
    'START': 'start',
    'HELP': 'help',
}
