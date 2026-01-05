from os import system

names = ["rahul", "rohan", "javed", "ritika" , "aditya"]

for name in names:
    system(f'powershell -Command "Add-Type -AssemblyName System.Speech; '
           f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'Shoutout to {name}\')"')