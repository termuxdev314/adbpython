import os

def run(command):
    os.system(f"adb shell {command}")

def root():
    os.system("adb root")

def ls():
    run(ls)

def pm(package, permission):
    run(f"pm grant {package} {permission}")
