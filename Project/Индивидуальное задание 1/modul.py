#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def strreplace(old, new):

    def helper(st):
        return st.replace(old, new)
    return helper