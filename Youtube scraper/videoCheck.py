import re

regex = re.compile(r'.*(THE CHILLUMINATI|DARK SOULS).*\/watch\?v=(.+)') # Compile regex

videoTitles = open('videoData.txt', 'r') # Open file
data = videoTitles.readlines() # Read file line by line

for line in data:
    mo = regex.search(line)

    if mo == None: # Skip files that don't match the regex
        continue
    
    print('Series: '+mo.group(1)+', Link: '+mo.group(2))
videoTitles.close()
print('videoCheck executed successfully!')