import json
import datetime

data = json.load(open("file.json"))
arrow = " --> "
limit = 8

timestamps = data["results"][0]["alternatives"][0]["timestamps"]

with open("file1.srt", "w") as f:
    words = []
    for i in range(len(timestamps)):
        line = timestamps[i]
        start = line[1]
        end = line[2]
        word = line[0]
        words.append(word + " ")
        print(words)
        f.write(str(i) + "\n")
        f.write(str(datetime.timedelta(seconds=start)).replace(".", ",")[0:-3] + arrow + str(datetime.timedelta(seconds=end)).replace(".", ",")[0:-3] + "\n")
        f.write("".join([x for x in words]) + "\n")
        f.write("\n")
        if len(words) == limit:
            words = []
