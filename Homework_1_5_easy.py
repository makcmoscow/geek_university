# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
def making_dir(x):
    # for x in range(0, 9):
    # os.mkdir('dir'+str(x))
    os.mkdir(x)
# import os
# for x in range(0, 9):
#     os.rmdir('dir'+str(x))
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
import os
def listing_dir():
    path = '.'
    for i in os.listdir(path):
        if os.path.isdir(os.path.join(path,i)):
            print(i)
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import os
import sys
def making_copy():
    full_name = sys.argv[0]
    name = str(full_name).split('/')[-1]
    with open(name+'_copy', 'w') as cp:
        with open(name, 'r', -1, 'utf-8') as f:
            for line in f:
                cp.write(line)

def deleting_dir(x):
    os.rmdir(x)