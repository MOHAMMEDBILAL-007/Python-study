import win32api
win32api.ShellExecute(
    0,
    "open",
    "notepad.exe"
    ,None
    ,None
    ,1
)