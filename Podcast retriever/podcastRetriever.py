import shutil, os, re

namePattern = re.compile(r'#(\d*\.?\d+)') # Compile regex
absWorkingDir = os.path.abspath('.') # Get the full, absolute file paths
dstFolder = "G:\#Audio\\" # Files will be copied to here
maxNumFiles = 8 # The maximum number of files to copy
count = 0 # Counting var

if os.path.isfile('./pyStorage.txt'): # Checks if storage exists
    storage = open('pyStorage.txt', 'r')
    lastEp = float(storage.read())
    storage.close()
else: # If storage doesn't exist, start over from 0. Re:Zero
    storage = open('pyStorage.txt', 'w')
    lastEp = 0

for filename in os.listdir('.'): # Loop over the files in the working directory
    mo = namePattern.search(filename)

    if mo == None: # Skip files that don't match the regex
        continue

    epNumber = float(mo.group(1)) # Grabs ep number, format: (#NN.NN)
    if (epNumber > lastEp) and (count < maxNumFiles): # Grabs latest episodes not listened to and copies them to dst
        print('Copying: '+ filename +'\nFrom: '+ absWorkingDir +'\nTo: '+ dstFolder)
        print('+---------------------------------+')
        filename = os.path.join(absWorkingDir, filename)
        shutil.copy(filename, dstFolder)
        count += 1

if not(storage.closed): # If the storage wasn't found
    storage.write(str(lastEp + maxNumFiles))
    storage.close()
else:
    storage = open('pyStorage.txt', 'w')
    storage.write(str(lastEp + maxNumFiles))
    storage.close()

if (count != maxNumFiles): # If there is no more audio left to listen, start over from 0
    os.unlink('./pyStorage.txt')