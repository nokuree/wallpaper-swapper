import os
import random
import ctypes


WALLPAPER_FOLDER = r'C:\wallpapers'

def get_wallpaper_list(folder):
    return [os.path.join(folder, f) for f in os.listdir(folder)
            if os.path.isfile(os.path.join(folder, f)) and f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]

def set_wallpaper(image_path):
    # SPI_SETDESKWALLPAPER = 20
    # SPIF_UPDATEINIFILE = 0x01
    # SPIF_SENDWININICHANGE = 0x02
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0x01 | 0x02)

def main():
    wallpapers = get_wallpaper_list(WALLPAPER_FOLDER)
    if wallpapers:
        wallpaper = random.choice(wallpapers)
        set_wallpaper(wallpaper)
    else:
        print("No wallpapers found in the specified folder.")

if __name__ == '__main__':
    main()
