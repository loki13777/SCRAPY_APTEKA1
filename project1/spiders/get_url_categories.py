# Получаем ссылки на категории из .txt файла c именами карегорий из сайта
import os
from project1.spiders.constants import START_URL

dict_replace_symbols = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z',
                        'и': 'i', 'к': 'k',
                        'л': 'l', 'м': 'm',
                        'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h',
                        'ц': 'ts', 'ч': 'ch',
                        'ш': 'sh', 'щ': 'shch', 'ы': 'y',
                        'э': 'e', 'ю': 'yu', 'я': 'ya', 'й': 'y', 'ъ': '', ' ': '-', '(': '_', ')': '_', ',': '_',
                        'ь': '', '.': '-',
                        '-': '_'}



def get_urls(name_file: str = 'input_categories.txt') -> list[str]:
    # открываем файл, читаем названия категорий на русском, заменяем символы на английские, склеиваем в ссылку
    # на категорию
    list_urls = []
    path_to_file = os.path.join(os.getcwd(), 'project1', 'spiders', name_file)
    with open(path_to_file, 'r') as f:
        file = f.read().split('\n')

    for string in file:
        string = string.lower()
        encrypted_str = ''
        for el in string:
            if el.isdigit():
                encrypted_str += el
            else:
                encrypted_str += dict_replace_symbols[el]

        list_urls.append(START_URL + '/catalog/' + encrypted_str)
    return list_urls
