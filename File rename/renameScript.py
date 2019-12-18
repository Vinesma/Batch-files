import shutil, os, re, sys, json

mainRegex = re.compile(r'(\[.+\]\s)([a-zA-Z0-9\'"@%+&()!. -]+)(\s.+)(\.mkv|\.mp4)')
videoFileRegex = re.compile(r'(\.mkv|\.mp4)')
absWorkingDir = os.path.abspath('.') # Get the absolute filepath for the working dir
chosenOption = 6

# Reading config files
try:
    if sys.platform == 'linux':
        with open("configLinux.json", "r") as readFile:
            destinationFolder, destinationFolder2 = json.load(readFile)
    else:
        with open("configWin.json", "r") as readFile:
            destinationFolder, destinationFolder2 = json.load(readFile)
except FileNotFoundError as err:
    print("[config] configuration not found, creating templates now.")
    template = ["<PATH to SEASONALS folder>", "<PATH to REGULAR EPS folder>"]
    with open("configLinux.json", "w") as openFile:
        json.dump(template, openFile)
    with open("configWin.json", "w") as openFile:
        json.dump(template, openFile)
    chosenOption = 5

# Renames, copies, then moves the file into a "./Watched/"
def renameCopyMove():
    # Checks if "./Watched/" exists, if not it is created
    if not(os.path.isdir(os.path.join('.', 'Watched'))):
        os.mkdir(os.path.join('.', 'Watched'))
    
    fileList = loopFilesInDir()
    for fileName in fileList:
        mo = mainRegex.search(fileName)

        if mo == None: # Skip files that don't match the regex
            continue

        fileTitle = mo.group(2)
        fileExtension = mo.group(4)
        newFileName = fileTitle + fileExtension

        fileName = os.path.join(absWorkingDir, fileName)
        newFileName = os.path.join(absWorkingDir, newFileName)
        print('Renaming: {}\nInto: {}'.format(fileName, newFileName))
        shutil.move(fileName, newFileName) # Rename
        print('Copying into: {}'.format(destinationFolder))
        shutil.copy(newFileName, destinationFolder) # Copy
        print('And moving into Watched folder')
        shutil.move(newFileName, os.path.join('.', 'Watched')) # Move
        print('+---------------------------------------+')

    print('RENAME/COPY/MOVE SCRIPT FINISHED!')
    if sys.platform != 'linux':
        input('Press ENTER to exit...')

# Renames the files, then copies them to a folder
def renameCopy():
    fileList = loopFilesInDir()
    for fileName in fileList:
        mo = mainRegex.search(fileName)

        if mo == None: # Skip files that don't match the regex
            continue

        fileTitle = mo.group(2)
        fileExtension = mo.group(4)
        newFileName = fileTitle + fileExtension

        fileName = os.path.join(absWorkingDir, fileName)
        newFileName = os.path.join(absWorkingDir, newFileName) # From

        print('Renaming: {}\nInto: {}'.format(fileName, newFileName))
        shutil.move(fileName, newFileName) # Rename
        print('Copying into: {}'.format(destinationFolder2))
        shutil.copy(newFileName, destinationFolder2) # Copy
        print('+---------------------------------------+')

    print('RENAME/COPY SCRIPT FINISHED!')
    if sys.platform != 'linux':
        input('Press ENTER to exit...')

def copy():
    # Copies the files to destinationFolder2
    fileList = loopFilesInDir()
    for fileName in fileList:
        mo = videoFileRegex.search(fileName) # Search for .mkv/.mp4 files

        if mo == None: # Skip files that don't match the regex
            continue

        fileName = os.path.join(absWorkingDir, fileName) # From
        print('Copying: {}\nTo: {}'.format(fileName, destinationFolder2))
        shutil.copy(fileName, destinationFolder2) # Copy
        print('+---------------------------------------+')

    print('COPY SCRIPT FINISHED!')
    if sys.platform != 'linux':
        input('Press ENTER to exit...')

def rename():
    # Renames files into their own dir   
    fileList = loopFilesInDir()
    for fileName in fileList:
        mo = mainRegex.search(fileName)

        if mo == None: # Skip files that don't match the regex
            continue

        fileTitle = mo.group(2)
        fileExtension = mo.group(4)
        newFileName = fileTitle + fileExtension

        fileName = os.path.join(absWorkingDir, fileName)
        newFileName = os.path.join(absWorkingDir, newFileName) # From
        print('Renaming: {}\nInto: {}'.format(fileName, newFileName))
        shutil.move(fileName, newFileName) # Rename
        print('+---------------------------------------+')

    print('RENAME SCRIPT FINISHED!')
    if sys.platform != 'linux':
        input('Press ENTER to exit...')

def loopFilesInDir():
    returnList = []
    for fileName in os.listdir('.'):
        returnList.append(fileName)
    return returnList

# START

while chosenOption == 6:
    print("Welcome! This is a script for moving my weeb shit to a flash drive:")
    print("[config] Your OS has been identified as: {}".format(sys.platform))
    print("1. Rename files, copy to USB and then store them in a folder called 'Watched'")
    print("2. Rename files and copy to USB")
    print("3. Copy (.mp4/.mkv) files to USB")
    print("4. Rename only")
    print("5. Exit")

    chosenOption = sys.stdin.readline()
    try:
        chosenOption = int(chosenOption)
    except ValueError as e:
        print("Please provide only numerical values.")
        chosenOption = 6

    if chosenOption == 1:
        renameCopyMove()
    elif chosenOption == 2:
        renameCopy()
    elif chosenOption == 3:
        copy()
    elif chosenOption == 4:
        rename()
    elif chosenOption == 5:
        print("Exiting script...")
    else:
        print("Unknown value...")
        chosenOption = 6