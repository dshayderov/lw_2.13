#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from modul import strreplace


if __name__ == '__main__':
    s = "Это строка для проверки программы"
    rep = strreplace('о', 'а')
    print(rep(s))