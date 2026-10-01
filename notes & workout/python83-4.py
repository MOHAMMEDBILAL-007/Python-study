import win32api
import win32process
import time 
# win32api.ShellExecute(
#     0,
#     "open",
#     "notepad.exe"
#     ,None
#     ,None
#     ,1
# )

# result = win32api.ShellExecute(0,"open","notepad.exe",None,None,1)
# print(result)
# import win32process
# import win32con
print(win32process.STARTUPINFO())

# result = win32process.CreateProcess(
#     None,
#     "notepad.exe",
#     None,
#     None,
#     False,
#     0,
#     None,
#     None,
#     win32process.STARTUPINFO()
# )
# result = win32process.CreateProcess(
#     "C:/Windows/System32/notepad.exe",
#     "notepad.exe",
#     None,
#     None,
#     False,
#     0,
#     None,
#     None,
#     win32process.STARTUPINFO()
# )
# print(result)

phandle,thandle,pid,tid=win32process.CreateProcess(
    "C:/Windows/System32/notepad.exe",
    "notepad.exe",
    None,
    None,
    False,
    0,
    None,
    None,
    win32process.STARTUPINFO()
)
print(phandle,thandle,pid,tid)
time.sleep(5)
win32api.CloseHandle(phandle)
win32api.CloseHandle(thandle)

win32api.CloseHandle(phandle)
win32api.CloseHandle(thandle)
print("handle closed")