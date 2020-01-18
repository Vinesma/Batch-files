import shutil, os, re, sys, json

# Regex
mainRegex = re.compile(r' ?([a-zA-Z0-9\'"@%+&()!.\s-]+-\s[0-9]+).*(\.mkv|\.mp4)')
videoFileRegex = re.compile(r'(\.mkv|\.mp4)')

# File Paths
tempFolder = 'temp'
watchedFolder = 'Watched'
absWorkingDir = os.path.abspath('.') # Get the absolute filepath for the working dir

tempFolderPath = os.path.join('.', tempFolder)
tempFolderWorkingDir = os.path.join(absWorkingDir, tempFolder)

watchedFolderPath = os.path.join('.', watchedFolder)
watchedFolderWorkingDir = os.path.join(absWorkingDir, watchedFolder)

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

# Functions
def searchFilesViaRegex(regex, directory):
    validFilesArray = []

    for fileName in allFilesIn(directory):
        mo = regex.search(fileName)
        
        if mo == None: # Skip files that don't match the regex
            continue

        validFilesArray.append(fileName)

    return validFilesArray

def allFilesIn(directory):
    fileArray = []

    for fileName in os.listdir(directory):
        fileArray.append(fileName)
        
    return fileArray

def destructureFileName(fileName, regex):
    mo = regex.search(fileName)

    fileTitle = mo.group(1)
    fileExtension = mo.group(2)
    newFileName = fileTitle + fileExtension

    return newFileName

def copyToTempFolder():
    createTempFolder()

    print('Copying files...')
    for filename in searchFilesViaRegex(videoFileRegex, absWorkingDir):
        copyTo(filename, tempFolderPath, False)
    print('Performing operations...')

def createTempFolder():
    print('Creating temporary folder...')
    os.mkdir(tempFolderPath)

def removeTempFolder():
    print('Cleaning up...')
    shutil.rmtree(tempFolderPath)

def renameInto(fileName, newFileName, log):
    if log:
        print('\nRenaming: [ {} ]\nInto: [ {} ]'.format(fileName, newFileName))
    shutil.move(fileName, newFileName) # Rename into

def copyTo(fileName, destination, log):
    if log:
        print('\nCopying [ {} ]\nto: [ {} ]'.format(fileName, destination))
    shutil.copy(fileName, destination) # Copy to

def moveIntoWatchedFolder(fileName):
    print('\nMoving [ {} ] into Watched folder'.format(fileName))
    shutil.move(fileName, watchedFolderWorkingDir)

def checkIfWatchedFolderExists():
    if not(os.path.isdir(watchedFolderPath)):
        os.mkdir(watchedFolderPath)

def inputIfLinux():
    if sys.platform != 'linux':
        input('\nPress ENTER to exit...')

def appendToWorkingDir(fileName):
    return os.path.join(tempFolderWorkingDir, fileName)

def clearScreen():
    os.system('clear' if sys.platform == 'linux' else 'cls')

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
        print("\nPlease provide only numerical values.")
        chosenOption = 0

    if chosenOption == 1:
        clearScreen()
        checkIfWatchedFolderExists()
        copyToTempFolder()

        print('[ RENAME/COPY/MOVE ]')
        for fileName in searchFilesViaRegex(mainRegex, tempFolderWorkingDir):
            newFileName = destructureFileName(fileName, mainRegex)

            fileName = appendToWorkingDir(fileName)
            newFileName = appendToWorkingDir(newFileName)
            
            renameInto(fileName, newFileName, True)
            copyTo(newFileName, destinationFolder, True)
            moveIntoWatchedFolder(newFileName)
            print('\n+----------------------------+')

        print('\nRENAME/COPY/MOVE SCRIPT FINISHED!')

        removeTempFolder()
        inputIfLinux()
        sys.exit()
    elif chosenOption == 2:
        clearScreen()
        copyToTempFolder()

        print('[ RENAME/COPY ]')
        for fileName in searchFilesViaRegex(mainRegex, tempFolderWorkingDir):
            newFileName = destructureFileName(fileName, mainRegex)

            fileName = appendToWorkingDir(fileName)
            newFileName = appendToWorkingDir(newFileName)

            renameInto(fileName, newFileName, True)
            copyTo(newFileName, destinationFolder2, True)
            print('\n+----------------------------+')

        print('\nRENAME/COPY SCRIPT FINISHED!')

        removeTempFolder()
        inputIfLinux()
        sys.exit()
    elif chosenOption == 3:
        clearScreen()

        print('[ COPY ]')
        for fileName in searchFilesViaRegex(videoFileRegex, absWorkingDir):
            fileName = appendToWorkingDir(fileName)

            copyTo(fileName, destinationFolder2, True)
            print('\n+----------------------------+')
        
        print('\nCOPY SCRIPT FINISHED!')

        inputIfLinux()
        sys.exit()
    elif chosenOption == 4:
        clearScreen()
        copyToTempFolder()

        print('[ RENAME ]')
        for fileName in searchFilesViaRegex(mainRegex, tempFolderWorkingDir):
            newFileName = destructureFileName(fileName, mainRegex)
            
            fileName = appendToWorkingDir(fileName)
            newFileName = appendToWorkingDir(newFileName)

            renameInto(fileName, newFileName, True)
            print('\n+----------------------------+')
        
        print('\nRENAME SCRIPT FINISHED!')

        removeTempFolder()
        inputIfLinux()
        sys.exit()
    elif chosenOption == 5:
        clearScreen()
        
        count = 1
        print('[ CURRENT FILES IN FOLDER: ]')
        for fileName in searchFilesViaRegex(videoFileRegex, absWorkingDir):
            print('\n{} : {}'.format(count, fileName))
            count += 1
        print('\n')
    elif chosenOption == 6:
        print("\nExiting script...")
        sys.exit()
    else:
        print("\nUnknown value...")