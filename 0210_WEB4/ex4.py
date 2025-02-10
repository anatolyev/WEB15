import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name")
parser.add_argument("-up", "--up_case", action="store_true",
                    help="Преобразование имени к верхнему регистру")
parser.add_argument("--number", choices=[1, 2, 3], type=int, default=1,
                    help="Выбери номер", required=True)
parser.add_argument("--no-name", action="store_const", const="no", dest="name")
arrgs = parser.parse_args()
name = arrgs.name
if (arrgs.up_case):
    name = name.upper()

print(f"Наше имя это {name}. И номер: {arrgs.number}")