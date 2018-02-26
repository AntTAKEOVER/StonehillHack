import subprocess
import os
import json

filename = "MHW2.mp4"
subprocess.run("ffmpeg -i " + filename + " -vn -acodec libmp3lame -ac 2 -ab 160k -ar 48000 audio.mp3", shell=True, check=True)
subprocess.run('curl -X POST -u 726561d0-cfb7-4fc5-ab28-c37af1622ad9:JGnLgWowu3t2 --header "Content-Type: audio/mp3" --data-binary @audio.mp3 "https://stream.watsonplatform.net/speech-to-text/api/v1/recognize?timestamps=true" -k -o file.json', shell=True, check=True)
os.remove("audio.mp3")
data = json.load(open("file.json"))
print(data["results"][0]["alternatives"][0]["transcript"])
os.remove("file.json")
