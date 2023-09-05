import subprocess
import os


if os.name == 'nt':
    subprocess.run('start "" "https://stackoverflow.com/q/321299"', shell=True)
elif os.name == 'posix':
    subprocess.run('xdg-open "https://stackoverflow.com/q/321299"', shell=True)
