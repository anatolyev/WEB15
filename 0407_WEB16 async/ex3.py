import time
from random import randint
ITER_NUM = 10
COROUT_NUM = 5

def do_some_work(i):
    for j in range(ITER_NUM):
        print(f"{i * ' '}{chr(9608)}{(COROUT_NUM-i)*' '}"
              f"Работник {i} прогресс: {j}{chr(9632) * j}")

def main():
    for i in range(COROUT_NUM):
        do_some_work(i)

if __name__ == '__main__':
    main()