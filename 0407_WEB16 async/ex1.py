import time
from datetime import datetime

COEFF = 1

def dish(num, prepare, wait):
    print(f"Начинаем готовить в {datetime.now().strftime('%H:%M:%S')} "
          f"блюдо №{num} будем готовить {prepare} минут(ы).")
    time.sleep(COEFF * prepare)
    print(f"продолжаем в {datetime.now().strftime('%H:%M:%S')} "
          f"ждать {wait} минут(ы) пока приготовится блюдо №{num} .")
    time.sleep(COEFF * wait)
    print(f"Закончили готовить в {datetime.now().strftime('%H:%M:%S')} "
          f"блюдо №{num}.")

def main():
    dish(1, 2, 3)
    dish(2, 5, 10)
    dish(3, 3, 5)

if __name__ == '__main__':
    t0 = time.time()
    main()
    delta = int((time.time() - t0) / COEFF)
    print(f"Все готово в {datetime.now().strftime('%H:%M:%S')} "
          f"было потрачено {delta} минут.")
