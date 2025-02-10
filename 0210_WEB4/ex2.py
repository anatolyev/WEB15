import argparse

parser = argparse.ArgumentParser()
parser.add_argument("all_args", metavar="Двоичные числа",
                    nargs='+', help="Двоичные числа будут преобразованы")
arrgs = parser.parse_args()
result = " ".join(map(lambda x: str(int(x, 2)), arrgs.all_args))
print(result)
