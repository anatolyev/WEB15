import argparse

parser = argparse.ArgumentParser()
parser.add_argument("arg1")
arrgs = parser.parse_args()
print(arrgs.arg1)
