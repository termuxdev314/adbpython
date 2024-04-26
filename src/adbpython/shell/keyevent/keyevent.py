import os
  
def keyevent(event):
  os.system(f"adb shell input keyevent {event}")
  
def soft_left():
  keyevent(1)
  
def soft_right():
  keyevent(2)
  
def home():
  keyevent(3)
  
def back():
  keyevent(4)
  
def call():
  keyevent(5)
  
def endcall():
  keyevent(6)
  
def key0():
  keyevent(7)
  
def key1():
  keyevent(8)
  
def key2():
  keyevent(9)
  
def key3():
  keyevent(10)
  
def key4():
  keyevent(11)
  
def key5():
  keyevent(12)
  
def key6():
  keyevent(13)
  
def key7():
  keyevent(14)
  
def key8():
  keyevent(15)
  
def key9():
  keyevent(16)
  
def star():
  keyevent(17)
  
def pound():
  keyevent(18)
  
def dpad_up():
  keyevent(19)
  
def dpad_down():
  keyevent(20)
  
def dpad_left():
  keyevent(21)
  
def dpad_right():
  keyevent(22)
  
def dpad_center():
  keyevent(23)

def volume_up():
  keyevent(24)
  
def volume_down():
  keyevent(25)

def power():
  keyevent(26)
  
def camera():
  keyevent(27)
  
def clear():
  keyevent(28)
  
def a():
  keyevent(29)
  
def b():
  keyevent(30)
  
def c():
  keyevent(31)
  
def d():
  keyevent(32)
  
def e():
  keyevent(33)
  
def f():
  keyevent(34)