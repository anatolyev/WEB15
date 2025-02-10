import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("all_args", metavar="Двоичные числа",
                    nargs='+', help="Двоичные числа будут преобразованы")
parser.add_argument("--base", default=2, type=int,
                    help="Система счисления по умолчанию")
parser.add_argument("--log", default=sys.stdout,
                    type=argparse.FileType('w'),
                    help="Нужно ввести имя файла для конвертированных значений")
arrgs = parser.parse_args()
result = " ".join(map(lambda x: str(int(x, arrgs.base)), arrgs.all_args))
arrgs.log.write(result + "\n")
print(result)
