
# -*- coding: utf-8 -*-

from enum import Enum

token = "490365717:AAF8A8jQigGJ2qDNoDAJpRhtRNiD_TjTQcU"
db_file = "database.vdb"
botan_key = 'd81377b5-3ec3-4463-bbca-3d9e309bc79d'

class States(Enum):
    """
    Мы используем БД Vedis, в которой хранимые значения всегда строки,
    поэтому и тут будем использовать тоже строки (str)
    """
    S_START = "0"  # Начало нового диалога
    S_ENTER_NAME = "1"
    S_ENTER_AGE = "2"
    S_SEND_PIC = "3"