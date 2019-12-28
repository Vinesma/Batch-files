import shutil, os, re, sys, json

mainRegex = re.compile(r'([a-zA-Z0-9\'"@%+&()!. ]+-[0-9 ]+).*(\.mkv|\.mp4)')
videoFileRegex = re.compile(r'(\.mkv|\.mp4)')
absWorkingDir = os.path.abspath('.') # Get the absolute filepath for the working dir
chosenOption = 0

# Reading config files
try:
    if sys.platform == 'linux':
        with open("configLinux.json", "r") as readFile:
            destinationFolder, destinationFolder2 = json.load(readFile)
    else:
        with open("configWin.json", "r") as readFile:
            destinationFolder, destinationFolder2 = json.load(readFile)
    print("[config] Config files loaded!")
except FileNotFoundError as err:
    print("[config] Configuration not found, creating templates now.")
    print("[config] Open the program again once it's properly configured.")
    template = ["<PATH to SEASONALS folder>", "<PATH to REGULAR EPS folder>"]
    with open("configLinux.json", "w") as openFile:
        json.dump(template, openFile)
    with open("configWin.json", "w") as openFile:
        json.dump(template, openFile)
    sys.exit()

def searchFilesViaRegex(regex):
    validFilesArray = []

    for fileName in filesInDir():
        mo = regex.search(fileName)

        if mo == None: # Skip files that don't match the regex
            continue

        validFilesArray.append(fileName)

    return validFilesArray

def filesInDir():
    fileArray = []

    for fileName in os.listdir('.'):
        fileArray.append(fileName)
        
    return fileArray

def destructureFileName(fileName, regex):
    mo = regex.search(fileName)

    fileTitle = mo.group(1)
    fileExtension = mo.group(2)
    newFileName = fileTitle + fileExtension

    return newFileName

def renameInto(fileName, newFileName):
    print('Renaming: [{}]\nInto: [{}]'.format(fileName, newFileName))
    shutil.move(fileName, newFileName) # Rename into

def copyTo(fileName, destination):
    print('Copying [{}] to: [{}]'.format(fileName, destinationFolder2))
    shutil.copy(fileName, destinationFolder2) # Copy to

def moveIntoWatchedFolder(fileName):
    print('Moving {} into Watched folder:'.format(fileName))
    shutil.move(fileName, os.path.join('.', 'Watched'))

def checkIfWatchedFolderExists():
    if not(os.path.isdir(os.path.join('.', 'Watched'))):
        os.mkdir(os.path.join('.', 'Watched'))

def inputIfLinux():
    if sys.platform != 'linux':
        input('Press ENTER to exit...')

def appendToWorkingDir(fileName):
    return os.path.join(absWorkingDir, fileName)

# START

while True:
    print("[config] OS: {}".format(sys.platform))
    print("Welcome! This is a script for moving my weeb shit to a flash drive:")
    print("1. Rename files, copy to USB and then store them in a folder called 'Watched'")
    print("2. Rename files and copy to USB")
    print("3. Copy (.mp4/.mkv) files to USB")
    print("4. Rename only")
    print("5. List (.mp4/.mkv) files in folder")
    print("6. Exit")

    chosenOption = sys.stdin.readline()
    try:
        chosenOption = int(chosenOption)
    except ValueError as e:
        print("Please provide only numerical values.")
        chosenOption = 0

    if chosenOption == 1:
        checkIfWatchedFolderExists()

        for fileName in searchFilesViaRegex(mainRegex):
            newFileName = destructureFileName(fileName, mainRegex)

            fileName = appendToWorkingDir(fileName)
            newFileName = appendToWorkingDir(newFileName)
            
            renameInto(fileName, newFileName)
            copyTo(newFileName, destinationFolder)
            moveIntoWatchedFolder(newFileName)

        print('RENAME/COPY/MOVE SCRIPT FINISHED!')

        inputIfLinux()
        sys.exit()
    elif chosenOption == 2:
        for fileName in searchFilesViaRegex(mainRegex):
            newFileName = destructureFileName(fileName, mainRegex)

            fileName = appendToWorkingDir(fileName)
            newFileName = appendToWorkingDir(newFileName)

            renameInto(fileName, newFileName)
            copyTo(newFileName, destinationFolder2)

        print('RENAME/COPY SCRIPT FINISHED!')

        inputIfLinux()
        sys.exit()
    elif chosenOption == 3:
        for fileName in searchFilesViaRegex(videoFileRegex):
            fileName = appendToWorkingDir(fileName)

            copyTo(fileName, destinationFolder2)
        
        print('COPY SCRIPT FINISHED!')

        inputIfLinux()
        sys.exit()
    elif chosenOption == 4:
        for fileName in searchFilesViaRegex(mainRegex):
            newFileName = destructureFileName(fileName, mainRegex)
            
            fileName = appendToWorkingDir(fileName)
            newFileName = appendToWorkingDir(newFileName)

            renameInto(fileName, newFileName)
        
        print('RENAME SCRIPT FINISHED!')

        inputIfLinux()
        sys.exit()
    elif chosenOption == 5:
        count = 1
        for fileName in searchFilesViaRegex(videoFileRegex):
            print('{} : {}'.format(count, fileName))
            count += 1
    elif chosenOption == 6:
        print("Exiting script...")
        sys.exit()
    else:
        print("Unknown value...")