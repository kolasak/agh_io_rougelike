import os
from distutils.dir_util import copy_tree
from shutil import copyfile, rmtree

if __name__ == "__main__":
    os.system('cmd /c "pyinstaller main.py --onefile"')
    if not os.path.exists("jakir"):
        os.mkdir("jakir")
    copyfile("dist/main.exe", "jakir/jakir.exe")
    copy_tree("images", "jakir/images")
    copyfile("config.json", "jakir/config.json")
    copyfile("riddles.json", "jakir/riddles.json")
    copyfile("freesansbold.ttf", "jakir/freesansbold.ttf")

    rmtree("build")
    rmtree("dist")
    os.remove("main.spec")