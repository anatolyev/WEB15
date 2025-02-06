#!/usr/bin/env python3.11
import sys

if len(sys.argv) > 1:
    print(f"Имя файла: {sys.argv[0]}\n"
        f"Первый аргумент: {sys.argv[1]}\n"
        f"Последний аргумент: {sys.argv[-1]}\n")
else:
    print(f"Наш файл: {sys.argv[0]} не содержит аргументов!")