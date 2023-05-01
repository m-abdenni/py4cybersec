import keyboard
import pyfiglet

banner = pyfiglet.figlet_format("Python Keylogger")
print(banner)

while True:
	keys = keyboard.record(until='ENTER')
	keyboard.play(keys)