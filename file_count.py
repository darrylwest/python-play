#!/usr/bin/env zxpy
# dpw@plaza.localdomain
# 2023-08-14 22:20:50

~"echo 'hello all'"

def print_file_count():
    count = ~'ls -1 | wc -l'

    print(f'file count = {count}')

print_file_count()
