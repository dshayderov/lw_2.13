#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def display_planes(staff):
    """
    Отобразить список самолетов.
    """
    # Проверить, что список самолетов не пуст.
    if staff:
        # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 15
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                "No",
                "Пункт назначения",
                "Номер рейса",
                "Тип самолета"
            )
        )
        print(line)

        # Вывести данные о всех самолетах.
        for idx, plane in enumerate(staff, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>15} |'.format(
                    idx,
                    plane.get('destination', ''),
                    plane.get('num', 0),
                    plane.get('typ', '')
                )
            )

        print(line)

    else:
        print("Список самолетов пуст")