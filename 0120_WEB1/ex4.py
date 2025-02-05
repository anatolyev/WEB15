import shutil
import os

shutil.copy("data/3/Описание.txt", "data/Описание - копия.txt")

print(os.getcwd())
# shutil.rmtree(os.getcwd() + "/data/1")
shutil.make_archive('archive', 'zip', root_dir='data')

