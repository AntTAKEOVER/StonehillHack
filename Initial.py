counter = 1
string = ""
import json

with open('file.json') as json_data:
    d = json.load(json_data)
    print("Start Time")
    print(d["results"][0]["alternatives"][0]["timestamps"][0][1])
    print("End Time")
    print(d["results"][0]["alternatives"][0]["timestamps"][-1][2])
    print(d["results"][0]["alternatives"][0]["transcript"])
    string += "{0}".format(counter) + "\n"
    string += "00:00:00,000 --> 00:00:00,750 \n"
    string += d["results"][0]["alternatives"][0]["timestamps"][0][0]
    counter = counter + 1 
    
    




print(string)
    

try:
    f = open("test.srt")
    for line in f: 
        continue
        #print(line, end = " ")
finally:
    
    f.close()
    

    
    
    

    


 
