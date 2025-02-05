from zipfile import ZipFile


with ZipFile("archive.zip") as myzip:
    myzip.printdir()
    with myzip.open('1.txt', 'r') as f:
        print(f.read().decode('utf8'))

with ZipFile("archive.zip", 'a') as myzip:
    myzip.write('ex1.json')
    print(myzip.namelist())