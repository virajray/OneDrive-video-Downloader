import subprocess

url=str(input("Enter that damned URl: "))
filename=str(input("Enter Name for this mf: "))
magic = "ffmpeg -i " + '\"' + url + '\"' + " -codec copy " + filename +".mp4"  
print(magic)
subprocess.run(magic, shell=True)
