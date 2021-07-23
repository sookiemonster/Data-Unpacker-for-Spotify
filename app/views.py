from app import app, spotify, ZipUploadForm
from collections import defaultdict
from datetime import datetime
from flask import render_template, request, abort
from json import loads
from sys import exc_info
from time import process_time
from zipfile import ZipFile

# allowed exts
ALLOWED_EXTENSIONS = ["zip"]

# frequency table
freqs = {
    "artist_freq": defaultdict(lambda: 0),
    "track_freq": defaultdict(lambda: 0),
    "hour_freq": defaultdict(lambda: 0),
    "days_freq": defaultdict(lambda: 0),
    "months_freq": defaultdict(lambda: 0),
}

# images for most-listened-to tracks / artists
top_track_img = []
top_artist_img = []

# user info
username = ""
user_icon_url = ""

# static vars
artistfreq = 10
trackfreq = 10
hourfreq = 10
daysfreq = 10
monthsfreq = 10

@app.template_filter()
def commaFormat(n):
    return f'{n:,}'

@app.route("/", methods=["GET", "POST"])
def homepage():
    start = process_time()

    # python scope rules demand i do this
    global username
    global user_icon_url

    # initialize form
    form = ZipUploadForm()

    if request.method == "GET":
        # render home template (upload page) and form
        return render_template("index.html", form=form)
    else:
        try:
            if form.validate_on_submit:
                # get zipfile from user
                file = request.files["file"]

                # secondary check to make sure file is a zip
                if file.filename.split(".")[-1] not in ALLOWED_EXTENSIONS:
                    abort(400)

                # create zip object
                zipfile_obj = ZipFile(file)

                # get a list of file names (json) inside zipfile
                namelist = zipfile_obj.namelist()
                file_names = [
                    file_name 
                    for file_name in namelist 
                    if file_name.endswith(".json")
                ]

                # make sure there are json files inside zip
                if not file_names:
                    abort(400)

                # make a list of tuples where the first element is the json encoded in a byte string
                # and the second element is the filename
                files = [
                    (zipfile_obj.open(name).read(), name)
                    for name in file_names
                    if name.split("/")[1].startswith("StreamingHistory")
                ]

                # make sure there are StreamingHistory jsons
                if not files:
                    abort(400)

                # convert byte string to dictionary
                files = [
                    loads(file[0].decode("UTF-8"))
                    for file in files
                ]

                # update and sort frequency table
                update([file for file in files])
                sort()

                # get user icon
                for name in file_names:
                    if name.split("/")[1].startswith("Userdata"):
                        try:
                            # load Identity.json file
                            info = loads(zipfile_obj.open(name).read().decode("UTF-8"))
                            user_id = info["username"]
                            user = spotify.user(user_id)
                            username = user["display_name"]
                            user_icon_url = user["images"][0]["url"]
                        except Exception as e:
                            print(e)
                            print("Something went wrong with getting user icon and/or username")
                            pass
                        
                
                # get images for most listened to tracks
                top_tracks = list(freqs["track_freq"].keys())[:trackfreq]
                for track in top_tracks:
                    try:
                        song = track.split(" by ")
                        results = spotify.search(q=f"{song[0]} {song[1]}", type="track")
                        url = results["tracks"]["items"][0]["album"]["images"][0]["url"]

                        top_track_img.append(url)
                    except Exception as e:
                        print(e)
                        print("Something went wrong with getting track images")
                        pass

                # get images for most listened to artists
                top_artists = list(freqs["artist_freq"].keys())[:artistfreq]
                for artist in top_artists:
                    try:
                        results = spotify.search(q=f"{artist}", type="artist")
                        results = results["artists"]["items"]

                        url = ""
                        for result in results:
                            if result["name"] == artist:
                                url = result["images"][0]["url"]
                                break
                    except Exception as e:
                        print(e)
                        print("Something went wrong with getting artist images")
                        pass

                    top_artist_img.append(url)

                # output to results page 
                return render_template(
                    'output.html',

                    # pass lists containing keys of the frequency table
                    artistkeys=top_artists,
                    trackkeys=top_tracks,
                    hourkeys=list(freqs["hour_freq"].keys())[:hourfreq],
                    dayskeys=list(freqs["days_freq"].keys())[:daysfreq],
                    monthskeys=list(freqs["months_freq"].keys())[:monthsfreq],

                    # pass lists containing values of the frequency table
                    artistvalues=list(freqs["artist_freq"].values())[:artistfreq],
                    trackvalues=list(freqs["track_freq"].values())[:trackfreq],
                    hourvalues=list(freqs["hour_freq"].values())[:hourfreq],
                    daysvalues=list(freqs["days_freq"].values())[:daysfreq],
                    monthsvalues=list(freqs["months_freq"].values())[:monthsfreq],

                    # pass track and artist counters
                    tracknum=len(freqs["track_freq"]),
                    artistnum=len(freqs["artist_freq"]),

                    # pass user info
                    display_name=username,
                    icon_url=user_icon_url,

                    # pass images for top tracks and artists
                    track_images=top_track_img,
                    artist_images=top_artist_img,

                    # pass zip function
                    zip=zip,
                )
        except Exception as e:
            print(e)
            print(f"{exc_info()[0]} occured")
            abort(500)
        finally:
            print(f"{(process_time() - start) * 1000} ms")

# update artist_freq and track_freq
def update(files):
    for file in files:
        for track in file:
            # convert end time to a datetime-readable format
            time = datetime.strptime(track["endTime"], "%Y-%m-%d %H:%M")

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