import json
from app import app
from ast import literal_eval
from datetime import datetime
from flask import render_template, request, redirect, jsonify
import zipfile

# frequency vars
artist_freq = {}
track_freq = {}
hour_freq = {}
days_freq = {}
months_freq = {}


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

            print(sorted(track_freq.items(), key=lambda x: x[1], reverse=True))

# update artist_freq and track_freq
def update(files):
    for file in files:
        for track in file:
            # convert end time to a datetime-readable format
            time = datetime.strptime(track["endTime"], "%Y-%m-%d %H:%M")

            update_artist_freq(track)
            update_track_freq(track)
            update_time_freq(time)

# try to increment item in artist_freq dictionary else add it
def update_artist_freq(track):
    try:
        artist_freq[track["artistName"]] += 1
    except KeyError:
        artist_freq[track["artistName"]] = 1

# try to increment item in track dictionary else add it
def update_track_freq(track):
    try:
        track_freq[track["trackName"] + " by " + track["artistName"]] += 1
    except KeyError:
        track_freq[track["trackName"] + " by " + track["artistName"]] = 1

# try to increment item in track dictionary else add it
def update_time_freq(time):
    try:
        hour_freq[time.hour] += 1
        days_freq[time.day] += 1
        months_freq[time.month] += 1
    except KeyError:
        hour_freq[time.hour] = 1
        days_freq[time.day] = 1
        months_freq[time.month] = 11