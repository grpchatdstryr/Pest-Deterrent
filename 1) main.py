import keyboard
from playsound import playsound
import subprocess

# In the terminal, you may have to install each of the above using: pip3 install <name>


print('Greetings! \n'
      'This program is meant for the nosy people who mess with your computer when you are not looking\n'
      'This program will do the following:\n'
      '- Display a load of "Stop Messing with Computer" images\n'
      '- Play a loud alarm that will certainly get attention\n'
      'I hope you enjoy!')


def anyKeyPress(lKey):

    # OPENS the IMAGE
    for i in range(0,10):
        subprocess.Popen(['start', r'C:\file\location\of\your\image.extension'], shell=True)


    # PLAYS ALARM in the BACKGROUND
    sound_file_path = r'C:\file\location\of\your\audio.extension'
    playsound(sound_file_path)


keyboard.on_press(anyKeyPress)
keyboard.wait()
