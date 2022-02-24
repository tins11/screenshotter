
from __future__ import print_function
import time 
import keyboard 

from desktopmagic.screengrab_win32 import (
getDisplayRects, saveScreenToBmp, saveRectToBmp, getScreenAsImage,
getRectAsImage, getDisplaysAsImages)

## Customization > > > > > > > > > > > > >
path = 'C:/tmp/screenshots/'    # define path where you want your screenshots to be written 
hotkey = 'ctrl+0'               # define your hot-key 
## Customization < < < < < < < < < < < < < 

print('Screenshot hotkey set as:', hotkey) 

def on_triggered(): 

    ## Generate timestamp when screenshot has been grabbed  
    timestamp = time.strftime('%Y-%m-%d_%H-%M-%S')

    ## Save the entire virtual screen as PNG
    entireScreen = getScreenAsImage()
    entireScreen.save(path + 'screenshot_' + timestamp + '.png', format='png')

    print('Saved screenshot: ' + path + 'screenshot_' + timestamp + '.png')

keyboard.add_hotkey(hotkey, on_triggered) 

print("Press ESC to stop screenshot process.") 
keyboard.wait('esc') 

