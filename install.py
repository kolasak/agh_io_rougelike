import os
from distutils.dir_util import copy_tree
from shutil import copyfile, rmtree

if __name__ == "__main__":
    os.system('cmd /c "pyinstaller main.py --onefile"')
    if not os.path.exists("app"):
        os.mkdir("app")
    copyfile("dist/main.exe", "app/jakir.exe")
    copy_tree("images", "app/images")
    copyfile("config.json", "app/config.json")
    copyfile("riddles.json", "app/riddles.json")
    copyfile("freesansbold.ttf", "app/freesansbold.ttf")

    rmtree("build")
    rmtree("dist")
    os.remove("main.spec")