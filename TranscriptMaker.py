import subprocess
import os
import json

filename = "EngVid.mp4"

subprocess.run("ffmpeg -i " + filename + " -vn -acodec libmp3lame -ac 2 -ab 160k -ar 48000 audio.mp3", shell=True, check=True)
subprocess.run('curl -X POST -u 726561d0-cfb7-4fc5-ab28-c37af1622ad9:JGnLgWowu3t2 --header "Content-Type: audio/mp3" --data-binary @audio.mp3 "https://stream.watsonplatform.net/speech-to-text/api/v1/recognize?timestamps=true" -k -o file.json')

#os.remove("audio.mp3")

data = json.load(open("file.json"))
print(data["results"][0]["alternatives"][0]["transcript"])

# b = 'curl -X POST --user 219c8fd3-9791-406a-9dc3-0c567c660298:HsB1NAPsZtLx --header "Accept: application/json" --data "{\\"text\\":\\' + '"' + data["results"][0]["alternatives"][0]["transcript"] + '\\"' + ',\\"source\\":\\"en\\",\\"target\\":\\"es\\"}" https://gateway.watsonplatform.net/language-translator/api/v2/translate -k -o transfile.json'
# subprocess.run(b)
# transdata = json.load(open("transfile.json"))
# data["results"][0]["alternatives"][0]["transcript"] = transdata["translations"][0]["translation"]
# with open("file.json", "w") as jsonFile:
#     json.dump(data, jsonFile)


#os.remove("file.json")
