from config.AutoMaticFolderEntry_config import Config
import keyboard


# shift + command + d,
# command + d,
# command + [,
# command + [,
# command + d,

keyboard.press_and_release("shift+command", "d")
keyboard.write(Config.server)
keyboard.wait('enter')
keyboard.write(Config.pw)