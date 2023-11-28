import win32api, win32con, sys
import ctypes
import rotatescreen
import time
from time import time, sleep, strftime
last = 0
user32 = ctypes.windll.User32
OpenDesktop = user32.OpenDesktopW
SwitchDesktop = user32.SwitchDesktop
DESKTOP_SWITCHDESKTOP = 0x0100
#print('checking status')
while True:
    hDesktop = OpenDesktop("default", 0, False, DESKTOP_SWITCHDESKTOP)
    result = SwitchDesktop(hDesktop)
    #print(result)
    if result:
#        print('unlocked')
        monitors = len(win32api.EnumDisplayMonitors())
        if monitors != last:
            last = monitors
            if monitors > 1:
 #               print("Docked")
                screens = rotatescreen.get_displays()
                screens[0].set_portrait()
            else:
  #              print("Not Docked")
                screen = rotatescreen.get_primary_display()
                screen.set_landscape()
    else:
         sleep(5)

    sleep(10)# - time() % 10)
        

#https://github.com/danny-burrows/rotate-screen#
