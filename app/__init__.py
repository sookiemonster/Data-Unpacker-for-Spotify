from flask import Flask,session,render_template,request,url_for,flash
from datetime import datetime
import os
import sqlite3
import json
import codecs
import glob
from werkzeug.utils import secure_filename


app = Flask(__name__, instance_path='/instance')
os.makedirs(os.path.join(app.instance_path, 'htmlfi'), exist_ok=True)


# freq vars
artist_freq = {}
track_freq = {}
end_freq = {}
files = [f for f in glob.glob("StreamingHistory**")]

# file upload 
ALLOWED_EXTENSIONS = {'zip'}



#page

@app.route("/",methods=['POST','GET']) 
def homepage():
    #add uploading logic
    if request.method == 'GET':
        return render_template('index.html')
    else:
        if request.files:
            f = request.files['datapackage']


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
    

@app.route("/output")
def output():
    


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
