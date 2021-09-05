#!/usr/bin/env python3

import json
import sys
import random

help_text = """
Show random proverb from json file. Add and manage proverbs in json file.
Json file - proverbs.json. That is in the same folder with proverb.py

website: http://kilinkarov.ru/proverbs

Format of the proverb object is:
[
    {
        'text': 'proverb text',
        'tags': ['tag1', 'tag2', 'etc.']
    }
]

Usage:
    proverbs.py - print random proverb from json file
    proverbs.py add - add new proverb to json file
    proverbs.py count - count all proverbs in json file
    proverbs.py --help - print this help


Copyright 2021 Alexander Kilinkarov

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


def add_proverb():
    with open('proverbs.json', 'r+', encoding='utf-8') as f:
        text = f.read()
        if text:
            proverbs = json.loads(text)
        else:
            proverbs = []

    proverb = dict()
    proverb['text'] = input('Введите пословицу или поговорку: ').strip()
    proverb['tags'] = [tag.strip() for tag in input('Введите теги (через запятую): ').split(',')]
    
    if not proverb['text']:
        print('Вы не ввели текст. Нечего добавлять.')
        return        
    
    for item in proverbs:
        if proverb['text'].lower() == item['text'].lower():
            print('Уже есть в базе')
            return
            
    proverbs.append(proverb)
    with open('proverbs.json', 'w', encoding='utf-8') as f:
        json.dump(proverbs, f, indent=1, ensure_ascii=False)
        
    print('Добавлено.')

def count_proverbs():
    with open('proverbs.json', 'r+', encoding='utf-8') as f:
        text = f.read()
        if text:
            proverbs = json.loads(text)
            if proverbs:
                return len(proverbs)
    return 0
    
    
def random_proverb():
    with open('proverbs.json', encoding='utf-8') as f:
        text = f.read()
        if text:
            proverbs = json.loads(text)
            if proverbs:
                return random.choice(proverbs)
    return False

if __name__ == '__main__':
    if '--help' in sys.argv:
        print(help_text)
    elif 'add' in sys.argv:
        add_proverb()
    elif 'count' in sys.argv:
        print(count_proverbs())
    elif len(sys.argv) == 1:
        proverb = random_proverb()
        if proverb:
            print(proverb['text'])
            print(*proverb['tags'], sep=', ')
        else:
            print('Что-то пошло не так. Наверное, в базе, пока что, нет пословиц.')
    else:
        print(help_text)
