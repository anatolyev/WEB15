import argparse

parser = argparse.ArgumentParser()
parser.add_argument("arg1")
parser.add_argument("arg2",
                    help="Какая то срока")
parser.add_argument("int_args", metavar="Кол-во аргументов",
                    type=int, nargs='+', help="Какие-то числа")
arrgs = parser.parse_args()

print(arrgs.arg1)
print(arrgs.arg2)
print(arrgs.int_args)