import shutil
import os


def selective_copy(folder, destination):
    """Write a program that walks through a folder tree and searches for files with a certain file extension (such as
    .pdf or .jpg). Copy these files from whatever location they are in to a new folder."""

    for foldernames, subfolders, filenames in os.walk(folder):
            for filename in filenames:
                if filename.endswith('.jpg') or filename.endswith('.pdf'):
                    os.makedirs(destination)
                    shutil.copy(os.path.abspath(filename), destination)


selective_copy('/home/bart/PycharmProjects/Python_Main/Automate the Boring Stuff/Project: Selective copy',
               '/home/bart/Documents/test')


