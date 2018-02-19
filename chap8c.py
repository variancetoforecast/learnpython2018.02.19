import os

DylanFolders = ['folder1', 'folder2']

for foldername in DylanFolders:
    print(os.path.join('/home/d/Desktop/learnpython', foldername))
    os.makedirs('/home/d/Desktop/learnpython/', foldername)


