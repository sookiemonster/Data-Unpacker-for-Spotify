from app import app
from ast import literal_eval
from collections import defaultdict
from datetime import datetime
from flask import render_template, request
import zipfile

# frequency table
freqs = {
    "artist_freq": defaultdict(lambda: 0),
    "track_freq": defaultdict(lambda: 0),
    "hour_freq": defaultdict(lambda: 0),
    "days_freq": defaultdict(lambda: 0),
    "months_freq": defaultdict(lambda: 0),
}

# static vars
artistfreq = 10
trackfreq = 10
hourfreq = 10
daysfreq = 10
monthsfreq = 10


@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "GET":
        # render home template (upload page)
        return render_template("index.html")
    else:
        if request.files:
            # get zipfile from user
            file = request.files["datapackage"]
            zipfile_obj = zipfile.ZipFile(file)

            # get a list of file names (json) inside zipfile
            namelist = zipfile_obj.namelist()
            file_names = [
                file_name 
                for file_name in namelist 
                if file_name.endswith(".json")
            ]

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

            # update and sort frequency table
            update([file for file in files])
            sort()

            # output to results page passing a paired list of keys and values with a limit
            return render_template(
                'output.html',
                artistkeys=list(freqs["artist_freq"].keys())[:artistfreq],
                trackkeys=list(freqs["track_freq"].keys())[:trackfreq],
                hourkeys=list(freqs["hour_freq"].keys())[:hourfreq],
                dayskeys=list(freqs["days_freq"].keys())[:daysfreq],
                monthskeys=list(freqs["months_freq"].keys())[:monthsfreq],
                artistvalues=list(freqs["artist_freq"].values())[:artistfreq],
                trackvalues=list(freqs["track_freq"].values())[:trackfreq],
                hourvalues=list(freqs["hour_freq"].values())[:hourfreq],
                daysvalues=list(freqs["days_freq"].values())[:daysfreq],
                monthsvalues=list(freqs["months_freq"].values())[:monthsfreq]
            )

# update artist_freq and track_freq
def update(files):
    for file in files:
        for track in file:
            # convert end time to a datetime-readable format
            time = datetime.strptime(track["endTime"], "%Y-%m-%d %H:%M")

            if track["artistName"] == "XXXTentacion":
                print(track)

            # increment freq by 1 else add new item
            freqs["artist_freq"][track["artistName"]] += 1
            freqs["track_freq"][track["trackName"] + " by " + track["artistName"]] += 1
            freqs["hour_freq"][time.hour] += 1
            freqs["days_freq"][time.weekday()] += 1
            freqs["months_freq"][time.month] += 1

# sort dicts in descending order
def sort():
    for key, value in freqs.items():
        freqs[key] = dict(
            sorted(value.items(), key=lambda x: x[1], reverse=True))