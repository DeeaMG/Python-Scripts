import os


# C:\\Users\\uic59362\\Desktop\\Python-Scripts-master\\Del_Duplicates\\testFolder
path = raw_input('Enter the path: ')
isCopy = ' - Copy'

fileDeleted = 0
for root, dirs, files in os.walk(path, topdown=True):
    for fileName in files:
        if isCopy in fileName:
            name = fileName.split(isCopy)[0]
            extension = os.path.splitext(fileName)[1]
            if name + extension in files:
                os.remove("{}\\{}".format(root, fileName))
                fileDeleted += 1
            elif isCopy + " (" in fileName:
                os.remove("{}\\{}".format(root, fileName))
                fileDeleted += 1

if fileDeleted:
    print('\nYou no longer have duplicates in this path!\nFiles deleted: {}'.format(fileDeleted))
else:
    print("You don't have duplicates.")
