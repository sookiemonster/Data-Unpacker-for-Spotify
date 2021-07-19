from app import app
from ast import literal_eval
from collections import defaultdict
from datetime import datetime
from flask import render_template, request
import zipfile

# frequency vars
artist_freq = defaultdict(lambda: 0)
track_freq = defaultdict(lambda: 0)
hour_freq = defaultdict(lambda: 0)
days_freq = defaultdict(lambda: 0)
months_freq = defaultdict(lambda: 0)

# static vars
trackfreqnum = 10

@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "GET":
        return render_template("index.html") # render home template
    else:
        if request.files:
            # get zipfile from user
            file = request.files["datapackage"]
            zipfile_obj = zipfile.ZipFile(file)

            # get a list of file names (json) inside zipfile
            namelist = zipfile_obj.namelist()
            file_names = [file_name for file_name in namelist if file_name.endswith(".json")]

            # make a list of tuples where the first element is the json encoded in a byte string
            # and the second element is the filename
            files = [
                (zipfile_obj.open(name).read(), name) 
                for name in file_names
                if name.split("/")[1].startswith("StreamingHistory")
            ]

            # convert byte string to dictionary
            files = [
                literal_eval(file[0].decode("UTF-8"))
                for file in files
            ]

            # update freq values
            update([file for file in files])

            trackfreqoutput = sorted(track_freq.items(), key=lambda x: x[1], reverse=True)
            return render_template('output.html', trackoutput = trackfreqoutput[:trackfreqnum])
            #return trackfreqoutput

# update artist_freq and track_freq
def update(files):
    for file in files:
        for track in file:
            # convert end time to a datetime-readable format
            time = datetime.strptime(track["endTime"], "%Y-%m-%d %H:%M")

            # increment freq by 1 else add new item
            artist_freq[track["artistName"]] += 1
            track_freq[track["trackName"] + " by " + track["artistName"]] += 1
            hour_freq[time.hour] += 1
            days_freq[time.weekday()] += 1
            months_freq[time.month] += 1