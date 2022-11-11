#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def get_plane():
    """
    Запросить данные о самолете.
    """
    destination = input("Пункт назначения: ")
    num = input("Номер рейса: ")
    typ = input("Тип самолета: ")

    # Создать словарь.
    return {
        'destination': destination,
        'num': num,
        'typ': typ,
    }