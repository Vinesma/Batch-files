import shutil, os, re

namePattern = re.compile(r'(\[.+\]\s)([a-zA-Z0-9. -]+)(\s.+)(\.mkv|\.mp4)') # Compile regex.

for filename in os.listdir('.'): # Loop over the files in the working directory.
    mo = namePattern.search(filename)

    if mo == None: # Skip files that don't match the regex.
        continue

    title = mo.group(2)
    extension = mo.group(4) # Get the different parts of the filename.

    newFilename = title + extension # Form the new filename.

    absWorkingDir = os.path.abspath('.') # Get the full, absolute file paths.
    print('Renaming: ' + filename + ' to: ' + newFilename)
    
    filename = os.path.join(absWorkingDir, filename)
    newFilename = os.path.join(absWorkingDir, newFilename)
    shutil.move(filename, newFilename) # Rename the files.