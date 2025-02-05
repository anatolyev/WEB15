import os

print(os.listdir('data'))

print()

for curdir, dirs, files in os.walk('data'):
    spacer = "    " * curdir.count("/")
    print(spacer + "📁" + str(curdir.split("/")[-1]))
    if files:
        for i in files:
            print(spacer + "    - " + i)
    # print(curdir, dirs, files)
