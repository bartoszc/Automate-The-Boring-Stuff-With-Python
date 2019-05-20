import os


def deleteUnneeded(folder):
    folder = os.path.abspath(folder)
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            fileSize = os.path.getsize(foldername + '/' + filename)
            if int(fileSize) < 10000000:
                continue
            # os.unlink(filename) #Commented out to protect against accidental deletion
            print('Deleting ' + filename + '...')  # Print only to verify working correctly


deleteUnneeded('/bart/Downloads')
