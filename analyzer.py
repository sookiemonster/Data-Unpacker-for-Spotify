import json
import codecs
import glob

def updateFreq(key, d):
    d[key] = d.get(key, 0) + 1

def updateTrackFreq(key, d, it):
    if not(key in d):
        d[key] = []
        d[key].append(it['artistName'])
        d[key].append(0)
    
    d[key][1] = d.get(key)[1] + 1

artist_freq = {}
track_freq = {}
end_freq = {}

files = [f for f in glob.glob("StreamingHistory**")]

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
    print(item)