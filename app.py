import subprocess

url = input("Enter the URL: ")
filename = input("Enter the filename: ")

command = f'ffmpeg -i "{url}" -codec copy "{filename}.mp4"'
print('Generated command: ' + command)

subprocess.run(command, shell=True)
