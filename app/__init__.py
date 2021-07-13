from flask import Flask,session
from flask import render_template
from flask import request
from datetime import datetime
import os
import sqlite3
import json
import codecs
import glob

app = Flask(__name__)


# freq vars
artist_freq = {}
track_freq = {}
end_freq = {}
files = [f for f in glob.glob("StreamingHistory**")]


#page

@app.route("/") 
def homepage():

    #add uploading logic

    for file in files:
        data_file = codecs.open(file, encoding='utf-8')
        json_array = json.load(data_file)

        for item in json_array:
            updateFreq(item['artistName'], artist_freq)
            updateFreq(item['endTime'], end_freq)
            updateTrackFreq(item['trackName'], track_freq, item)

        data_file.close()

    top_tracks = list(sorted(track_freq.items(), key = lambda x : x[1][1], reverse=True)[:10])

    for item in top_tracks:
        print(item) #move this to output

    return render_template('index.html')



#non-page 

def updateFreq(key, d):
    d[key] = d.get(key, 0) + 1

def updateTrackFreq(key, d, it):
    if not(key in d):
        d[key] = []
        d[key].append(it['artistName'])
        d[key].append(0)
    
    d[key][1] = d.get(key)[1] + 1



    
if __name__ == "__main__":
    app.debug = True 
    app.run()
