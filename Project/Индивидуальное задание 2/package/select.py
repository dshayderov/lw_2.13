#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def select_planes(staff, jet):
    """
    Выбрать самолеты с заданным типом.
    """
    # Сформировать список самолетов.
    result = [plane for plane in staff if jet == plane.get('typ', '')]

    # Возвратить список выбранных самолетов.
    return result