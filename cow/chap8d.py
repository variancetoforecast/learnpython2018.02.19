import os

print(os.listdir(os.getcwd()))

DylansFolder = os.listdir(os.getcwd())

for foldername in DylansFolder:
    print(os.path.basename(foldername))
    NewName = os.path.basename(foldername) + 'hash'
    print(os.path.basename(foldername))