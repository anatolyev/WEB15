import logging

def log():
    i = 0
    while i < 10:
        logging.warning(i)
        i += 1

def log2():
    logging.debug("Отладка")
    logging.info("Информация")
    logging.warning("ВНИМАНИЕ")
    logging.error("Ошибка")
    logging.critical("Критическая или фатальная ошибка")


if __name__ == '__main__':
    logging.basicConfig(
        filename="ex1.log",
        format="%(asctime)s %(levelname)s %(name)s %(message)s"
    )
    log2()


