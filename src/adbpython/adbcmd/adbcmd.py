import os

def run(command):
    os.system(f"adb {command}")

def install(package, path):
    os.chdir(path)
    os.system(f"adb install {package}")
