import time
from datetime import datetime
import asyncio
import os


COEFF = 1

async def dish(num, prepare, wait):
    print(f"Начинаем готовить в {datetime.now().strftime('%H:%M:%S')} "
          f"блюдо №{num} будем готовить {prepare} минут(ы).")
    time.sleep(COEFF * prepare)
    print(f"продолжаем в {datetime.now().strftime('%H:%M:%S')} "
          f"ждать {wait} минут(ы) пока приготовится блюдо №{num} .")
    await asyncio.sleep(COEFF * wait)
    print(f"Закончили готовить в {datetime.now().strftime('%H:%M:%S')} "
          f"блюдо №{num}.")

async def main():
    task = [
    asyncio.create_task(dish(2, 5, 10)),
    asyncio.create_task(dish(3, 3, 5)),
    asyncio.create_task(dish(1, 2, 3)),
    ]
    await asyncio.gather(*task)

if __name__ == '__main__':
    t0 = time.time()
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
    delta = int((time.time() - t0) / COEFF)
    print(f"Все готово в {datetime.now().strftime('%H:%M:%S')} "
          f"было потрачено {delta} минут.")
