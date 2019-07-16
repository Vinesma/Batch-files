import shutil, os, re, sys

namePattern = re.compile(r'(\[.+\]\s)([a-zA-Z0-9. -]+)(\s.+)(\.mkv|\.mp4)') # Compile regex
namePattern2 = re.compile(r'(\.mkv|\.mp4)') # Compile regex
dstFolder = "G:\#Video\Seasonals\\" # Destination folder
dstFolder2 = "G:\#Video\\" # Destination folder 2
absWorkingDir = os.path.abspath('.') # Working dir
opt = 5 # Options

def loopDir():
    returnList = []
    for filename in os.listdir('.'):
        returnList.append(filename)
    return returnList


def renameCopyMoveFunc():
    if not(os.path.isdir('.\\Watched\\')):
        os.mkdir('.\\Watched\\')
    
    fileList = loopDir()
    for filename in fileList:
        mo = namePattern.search(filename) # Search for the regex

        if mo == None: # Skip files that don't match the regex
            continue

        title = mo.group(2)
        extension = mo.group(4) # Get the different parts of the filename

        newFilename = title + extension # Form the new filename

        print('Renaming: '+ filename +'\nInto: '+ newFilename + '\nCopying into: '+ dstFolder +'\nAnd moving into Watched folder')
        print('+---------------------------------------+')

        filename = os.path.join(absWorkingDir, filename) 
        newFilename = os.path.join(absWorkingDir, newFilename) # From
        shutil.move(filename, newFilename) # Rename
        shutil.copy(newFilename, dstFolder) # To
        shutil.move(newFilename, '.\\Watched\\') # Move
    print('RENAME/COPY/MOVE SCRIPT FINISHED!')

def renameCopyFunc():   
    fileList = loopDir()
    for filename in fileList:
        mo = namePattern.search(filename) # Search for the regex

        if mo == None: # Skip files that don't match the regex
            continue

        title = mo.group(2)
        extension = mo.group(4) # Get the different parts of the filename

        newFilename = title + extension # Form the new filename

        print('Renaming: '+ filename +'\nInto: '+ newFilename + '\nAnd copying into: '+ dstFolder2)
        print('+---------------------------------------+')

        filename = os.path.join(absWorkingDir, filename) 
        newFilename = os.path.join(absWorkingDir, newFilename) # From
        shutil.move(filename, newFilename) # Rename
        shutil.copy(newFilename, dstFolder2) # To
    print('RENAME/COPY SCRIPT FINISHED!')

def copyFunc():
    fileList = loopDir()
    for filename in fileList:
        mo = namePattern2.search(filename) # Search for .mkv/.mp4 files

        if mo == None: # Skip files that don't match the regex
            continue

        print('Copying: '+ filename +'\nTo: '+ dstFolder2)
        print('+---------------------------------------+')

        filename = os.path.join(absWorkingDir, filename) # From
        shutil.copy(filename, dstFolder2) # To
    print('COPY SCRIPT FINISHED!')

while opt == 5: 
    print("Welcome! This is a script for moving my weeb shit to a flash drive:")
    print("1. Rename files, copy to USB and then store them in a folder called 'Watched'")
    print("2. Rename files and copy to USB")
    print("3. Copy to USB")
    print("4. Exit")

    opt = sys.stdin.readline()
    try:
        opt = int(opt)
    except ValueError as e:
        print("Please provide only numerical values.")
        opt = 5

    if opt == 1:
        renameCopyMoveFunc()
    elif opt == 2:
        renameCopyFunc()
    elif opt == 3:
        copyFunc()
    elif opt == 4:
        print("Exiting script...")
    else:
        print("Unknown value...")
        opt = 5