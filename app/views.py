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
artistfreq = 10
trackfreq = 10
hourfreq = 10
daysfreq = 10
monthsfreq = 10
            

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

            artistfreqkeys = sorted(artist_freq.items(), key=lambda x: x[1], reverse=True)
            trackfreqkeys = sorted(track_freq.keys(), key=lambda x: x[1], reverse=True)
            hourfreqkeys = sorted(hour_freq.keys(), key=lambda x: x[1], reverse=True)
            daysfreqkeys = sorted(days_freq.keys(), key=lambda x: x[1], reverse=True)
            monthsfreqkeys = sorted(months_freq.keys(), key=lambda x: x[1], reverse=True)

            artistfreqvalues = sorted(artist_freq.values(), key=lambda x: x[1], reverse=True)
            trackfreqvalues = sorted(track_freq.values(), key=lambda x: x[1], reverse=True)
            hourfreqvalues = sorted(hour_freq.values(), key=lambda x: x[1], reverse=True)
            daysfreqvalues = sorted(days_freq.values(), key=lambda x: x[1], reverse=True)
            monthsfreqvalues = sorted(months_freq.values(), key=lambda x: x[1], reverse=True)

            print(trackfreqkeys[:trackfreq])
            return render_template('output.html', artistkeys = artistfreqkeys[:artistfreq], trackkeys = trackfreqkeys[:trackfreq], hourkeys = hourfreqkeys[:hourfreq], dayskeys = daysfreqkeys[:daysfreq], monthskeys = monthsfreqkeys[:monthsfreq], artistvalues = artistfreqvalues[:artistfreq], trackvalues = trackfreqvalues[:trackfreq], hourvalues = hourfreqvalues[:hourfreq], daysvalues = daysfreqvalues[:daysfreq], monthsvalues = monthsfreqvalues[:monthsfreq])
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