## ScreenShotter 
 
ScreenShotter Python script allows one to grab a screenshot of all desktops by pressing hotkey. After this, the screenshot is written into given path with timestamp for later use. 


#### Installation 
1. Install Desktopmagic `pip install Desktopmagic`. See help from [Desktopmagic](https://pypi.org/project/Desktopmagic/) page. 
2. Install keyboard `pip install keyboard`. See example [here](https://stackoverflow.com/questions/48915822/creating-a-hotkey-to-enter-text-using-python-running-in-background-waiting-for). 


#### Configuration 
You can modify hotkey buttons and path where the screenshots are written according to your preferences. To do this, adjust lines #11-12 from screenshotter.py code. 

`path = 'C:/tmp/screenshots/` 
 
`hotkey = 'ctrl+0'` 

Please **make sure that path really exists**. 


#### Usage 
1. Start program and let it run on background. 
2. Press hotkey (default `CTRL+0`) whenever to grab a screenshot. 
3. Go to screenshot folder to see the freshly captured screenshot (default *C:/tmp/screenshots/*)


Happy screencapturing! 


#### Limitations 
Desktopmagic package does not recognize or care about different screen resolutions if one has multiple monitors. 
Hence, the final output seems to be rectangle according to height of primary monitor's resolution. 


#### License 
The MIT License (MIT)