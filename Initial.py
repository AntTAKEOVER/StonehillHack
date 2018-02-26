try:
    f = open("test.srt")
    for line in f: 
        print(line, end = " ")
   
    f.seek(0) 
    
    
finally:
    
    f.close()
    


 
