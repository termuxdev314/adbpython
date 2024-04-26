import os

def connect(ip, port):
    os.system(f"adb connect {ip}:{port}")

def disconnect(ip):
    os.system(f"adb disconnect {ip}")
