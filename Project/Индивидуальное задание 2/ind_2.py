#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import sys
from package.add import get_plane
from package.list import display_planes
from package.select import select_planes
from package.help import help


def main():
    """
    Главная функция программы.
    """
    # Список самолетов.
    planes = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о самолете.
            plane = get_plane()

            # Добавить словарь в список.
            planes.append(plane)
            # Отсортировать список в случае необходимости.
            if len(planes) > 1:
                planes.sort(key=lambda item: item.get('destination', ''))

        elif command == 'list':
            # Отобразить все самолеты.
            display_planes(planes)

        elif command.startswith('select '):
            # Разбить команду на части для выделения пункта назначения.
            part = command.split(' ', maxsplit=1)
            com = part[1]

            # Выбрать самолеты заданного типа
            selected = select_planes(planes, com)
            # Отобразить выбранные самолеты
            display_planes(selected)

        elif command == 'help':
            help()
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()