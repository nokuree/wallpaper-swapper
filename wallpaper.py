# Program executes at startup

import os
import random
import ctypes
import json 

WALLPAPER_FOLDER = r'C:\wallpapers'

# So we open up the .json file we will use to track our wallpapers
APPDATA_DIR = os.getenv('APPDATA')
TRACK_FILE = os.path.join(APPDATA_DIR, 'wallpaper_rotator', 'used_wallpapers.json')

# gets wallpapers
def get_wallpaper_list(folder):
    return [os.path.join(folder, f) for f in os.listdir(folder)
            if os.path.isfile(os.path.join(folder, f)) and f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]

# Sets wallpaper in the OS
def set_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0x01 | 0x02)

# We read from the json file 
def load_used_wallpaper():
    if not os.path.exists(TRACK_FILE):
        return []
    try:
        with open(TRACK_FILE, 'r') as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return []

# Write to the json file
def save_used_wallpapers(used_wallpapers):
    os.makedirs(os.path.dirname(TRACK_FILE), exist_ok=True)
    with open(TRACK_FILE, 'w') as file:
        json.dump(used_wallpapers, file)

def main():
    # So we get the wallpapers from our folder
    wallpapers = get_wallpaper_list(WALLPAPER_FOLDER)
    if not wallpapers:
        print("No wallpapers found here!")
        return
    
    # get our used wallpapers
    used_wallpapers = load_used_wallpaper()

    # python nonsense that im suprised that works lol, reads from the file and places it in the array 
    unused_wallpapers = [wp for wp in wallpapers if wp not in used_wallpapers]

    # So if we use all the wallpapers up, then we rest the json file 
    if not unused_wallpapers:
        used_wallpapers =  []
        unused_wallpapers = wallpapers.copy()
        print("Used all wallpapers, resetting the rotation!")

    # Select one of the unused wallpaers randomly 
    selected_wallpaper = random.choice(unused_wallpapers)
    set_wallpaper(selected_wallpaper)

    # We update the used wallpapers
    used_wallpapers.append(selected_wallpaper)
    save_used_wallpapers(used_wallpapers)


if __name__ == '__main__':
    main()
