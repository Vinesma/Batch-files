import shutil, os, re, sys

dstFolder = os.path.join('/', 'media', 'vinesma', 'B2A6-5374', '#Video', 'Seasonals') # Destination folder
dstFolder2 = os.path.join('/', 'media', 'vinesma', 'B2A6-5374', '#Video') # Destination folder 2

namePattern = re.compile(r'(\[.+\]\s)([a-zA-Z0-9\'"@%+&()!. -]+)(\s.+)(\.mkv|\.mp4)') # Compile regex
namePattern2 = re.compile(r'(\.mkv|\.mp4)') # Compile regex
absWorkingDir = os.path.abspath('.') # Get the absolute filepath for the working dir
opt = 5 # Options

def loopDir():
    # Loop between all the files in the current dir
    # Returns a List
    returnList = []
    for filename in os.listdir('.'):
        returnList.append(filename)
    return returnList

def renameCopyMoveFunc():
    # Renames, copies, then moves the file into a "Watched" folder
    if not(os.path.isdir(os.path.join('.', 'Watched'))):
        os.mkdir(os.path.join('.', 'Watched'))
    
    fileList = loopDir()
    for filename in fileList:
        mo = namePattern.search(filename) # Search for the regex

        if mo == None: # Skip files that don't match the regex
            continue

        title = mo.group(2)
        extension = mo.group(4) # Get the different parts of the filename

        newFilename = title + extension # Form the new filename

        filename = os.path.join(absWorkingDir, filename)
        newFilename = os.path.join(absWorkingDir, newFilename) # From
        print('Renaming: {}\nInto: {}'.format(filename, newFilename))
        shutil.move(filename, newFilename) # Rename
        print('Copying into: {}'.format(dstFolder))
        shutil.copy(newFilename, dstFolder) # To
        print('And moving into Watched folder')
        shutil.move(newFilename, os.path.join('.', 'Watched')) # Move
        print('+---------------------------------------+')
    print('RENAME/COPY/MOVE SCRIPT FINISHED!')
    input('Press ENTER to exit...')

def renameCopyFunc():
    # Renames the files
    fileList = loopDir()
    for filename in fileList:
        mo = namePattern.search(filename) # Search for the regex

        if mo == None: # Skip files that don't match the regex
            continue

        title = mo.group(2)
        extension = mo.group(4) # Get the different parts of the filename

        newFilename = title + extension # Form the new filename

        filename = os.path.join(absWorkingDir, filename)
        newFilename = os.path.join(absWorkingDir, newFilename) # From
        print('Renaming: {}\nInto: {}'.format(filename, newFilename))
        shutil.move(filename, newFilename) # Rename
        print('+---------------------------------------+')
    print('RENAME SCRIPT FINISHED!')
    input('Press ENTER to exit...')

def copyFunc():
    # Copies the files to dstFolder2
    fileList = loopDir()
    for filename in fileList:
        mo = namePattern2.search(filename) # Search for .mkv/.mp4 files

        if mo == None: # Skip files that don't match the regex
            continue

        filename = os.path.join(absWorkingDir, filename) # From
        print('Copying: {}\nTo: {}'.format(filename, dstFolder2))
        shutil.copy(filename, dstFolder2) # To
        print('+---------------------------------------+')
    print('COPY SCRIPT FINISHED!')
    input('Press ENTER to exit...')

# START

while opt == 5: 
    print("Welcome! This is a script for moving my weeb shit to a flash drive:")
    print("1. Rename files, copy to USB and then store them in a folder called 'Watched'")
    print("2. Only rename files")
    print("3. Only copy to USB")
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