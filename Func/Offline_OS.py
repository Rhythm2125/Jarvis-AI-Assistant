import os
import subprocess as sp

paths = {
    'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
    'discord': "C:\\Users\\rhyth\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe",
    'chrome': "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
    'word': 'C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE',
}

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def open_notepad():
    os.startfile(paths['notepad'])

def open_discord():
    os.startfile(paths['discord'])

def open_cmd():
    os.system('start cmd')

def open_calculator():
    sp.Popen(paths['calculator'])

def open_chrome():
    os.startfile(paths['chrome'])

def open_word():
    os.startfile(paths['word'])

def access_software(software_name, command):
    try:
        cmd = f"{software_name} {command}"
        output = sp.check_output(cmd, shell=True)
        return output.decode("utf-8").strip()
    except sp.CalledProcessError as e:
        print(f"Error accessing {software_name}: {e}")
        return None
