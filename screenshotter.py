#ch8_screenshotter.py

import win32api
import win32ui
import win32gui
import win32con

# Replace filePath
filepath = r"C:\Users\MyUser\Desktop\example.bmp"
width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

handle_desktop = win32gui.GetDesktopWindow()
dc_desktop = win32gui.GetWindowDC(handle_desktop)
dc_img = win32ui.CreateDCFromHandle(dc_desktop)

dc_mem = dc_img.CreateCompatibleDC()

screenshot = win32ui.CreateBitmap()
screenshot.CreateCompatibleBitmap(dc_img, width, height)
dc_mem.SelectObject(screenshot)

print(dc_mem)
dc_mem.BitBlt((0, 0), (width, height), dc_img, (left, top), win32con.SRCCOPY)
screenshot.SaveBitmapFile(dc_mem , filepath)

dc_mem.DeleteDC()
win32gui.DeleteObject(screenshot.GetHandle())
