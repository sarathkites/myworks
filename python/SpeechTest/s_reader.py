import speech_recognition as sr
import sqlite3 as lite
import os
import time

def wavparser(file_path):
    
    print(sr.__version__)
    r = sr.Recognizer()
    audio_file = sr.AudioFile(file_path)
    with audio_file as source:
        audio = r.record(source)
    #print(type(audio))
    res = r.recognize_google(audio)
    return res
def fetchwords(dbfile):
    con = lite.connect(dbfile)
    words = list()
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM word_details")
        rows = cur.fetchall()
        for row in rows:
            words.append(row[1])
    #        print( row[1])
            
    return words
            
def search_and_move(words,txt):
    
    for word in words:
        pos = txt.find(word)
        if pos != -1 :
            filename = str(int(time.time()*1000.0))+'.txt'
            path = './record/'+word+"/"
            os.makedirs(path);
            f= open(path+filename,"w+")
            f.write(txt)
            f.close()

txt = wavparser('harvard.wav')
print(txt)
#print(res.find('Bihar'))
words = fetchwords('words.db')
print(words)
search_and_move(words, txt)
print("Done")
