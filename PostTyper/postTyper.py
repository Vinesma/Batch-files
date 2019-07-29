import pyautogui, os, time

pyautogui.PAUSE = 0.5 #Protection in case something goes wrong, press CTRL + C to stop the program
pyautogui.FAILSAFE = True

sleepSec = 5 # Number of seconds to sleep before running program
for i in range(sleepSec): # Gives the user time to move the cmd window out of the way
    time.sleep(1)
    print(i + 1)

boxPos = pyautogui.locateOnScreen('respBox.png') # Find the location of this image on the screen
btnPos = pyautogui.locateOnScreen('saveBtn.png')

if os.path.isfile('./input.txt'): # Checks if a text file exists

    txtFile = open('input.txt', 'r')
    msgContent = txtFile.read() # Grabs the contents of the file
    txtFile.close()

    try:
        if (len(msgContent) < 1): # If there's no content in the file
            print('ATTENTION, the txt file is empty of content!')
            raise Exception
        if ((btnPos == None) or (boxPos == None)): # If the button/Box is unable to be found 
            print('Unable to find button / response box... consider changing the image files loaded.')
            raise Exception

        centerBox = pyautogui.center(boxPos)
        pyautogui.click(centerBox) # Find the center and click
        pyautogui.typewrite(msgContent, 0.20) # Type contents
        centerBtn = pyautogui.center(btnPos)
        pyautogui.click(centerBtn) # Find the center and clicks to post!

        txtFile = open('input.txt', 'w') #Delete contents of input.txt
        txtFile.close()
    except Exception:
        print('Error! Press enter to exit.')
        input()
else:
    print('Unable to locate input.txt file, creating one now.')
    txtFile = open('input.txt', 'w')
    txtFile.close()
    print('Press enter to exit.')
    input()
