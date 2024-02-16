"""
Архив data.zip содержит различные папки и файлы. Среди них есть несколько JSON файлов,
каждый из которых содержит информацию о каком-либо футболисте. Программа обрабатывает
только данные JSON файлы и выводит имена и фамилии футболистов, выступающих за футбольный
клуб Arsenal. Футболисты по окончании расположены в лексикографическом порядке имен,
а при совпадении — в лексикографическом порядке фамилий, каждый на отдельной строке.
!!! Наличие у файла расширения .json не гарантирует, что он является корректным текстовым
файлом в формате JSON !!!
"""


import os.path
from zipfile import ZipFile
import json


def is_correct_json(file_name):
    try:
        players = json.load(file_name)
        return players
    except ValueError:
        return {}


with ZipFile('../testing_data/data.zip') as zip_file:
    players_lst = []
    for i in zip_file.namelist():
        if os.path.basename(i).split('.')[-1] == 'json':
            with zip_file.open(i, 'r') as file:
                player = is_correct_json(file)
                if player:
                    if player['team'] == 'Arsenal':
                        players_lst.append(str(player['first_name'] + ' ' + player['last_name']))
    print(*sorted(players_lst), sep='\n')
