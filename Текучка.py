"""
Имеется набор файлов, каждый из которых, кроме последнего,
содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.
"""

import requests


def get_file(file_url):
    """Печатает файл, начинающийся с 'We', или рекурентно вызывает себя"""
    # print('file_url: ', file_url)
    file = requests.get(file_url)
    if file.text[:2] == 'We':
        print(file.text)
    else:
        # next_file_name = file.text.strip()
        # print('next_file_url:', next_file_url)
        get_file('https://stepic.org/media/attachments/course67/3.6.3/' +
                 file.text.strip())
    pass

with open('dataset_3378_3.txt') as f:
    init_file_url = f.read().strip()
    # print('init_file_name: ', init_file_url)
    get_file(init_file_url)
