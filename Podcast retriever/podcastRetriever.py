import shutil, os, re

namePattern = re.compile(r'#(\d*\.?\d+)') # Compile regex
absWorkingDir = os.path.abspath('.') # Get the full, absolute file paths
maxNumFiles = 8 # The maximum number of files to copy
count = 0 # Counting var

if os.path.isfile('./pyStorage.txt'): # Checks if storage exists
    storage = open('pyStorage.txt', 'r')
    c = float(storage.read())
    storage.close()
else:
    storage = open('pyStorage.txt', 'w')
    c = 0
    
for filename in os.listdir('.'): # Loop over the files in the working directory
    mo = namePattern.search(filename)

    if mo == None: # Skip files that don't match the regex
        continue

    epNumber = float(mo.group(1)) # Grabs the episode number
    if (epNumber > c) and (count < maxNumFiles): # Grabs the latest episodes not listened to
        print('Copying: '+ filename +'\nFrom: '+ absWorkingDir +'\nTo: G:\#Audio\\')
        filename = os.path.join(absWorkingDir, filename)        
        shutil.copyfile(filename, 'G:\\#Audio\\') # DOESN'T WORK
        count += 1

# if count != maxNumFiles: # If there is no more audio left to listen, start over from 0 WIP
    # os.unlink(os.path('./pyStorage.txt'))

if not(storage.closed): # If the storage wasn't found
    storage.write(str(c + maxNumFiles))
    storage.close()
else:
    storage = open('pyStorage.txt', 'w')
    storage.write(str(c + maxNumFiles))
    storage.close()

# print(maxNumFiles)
# print(count)
