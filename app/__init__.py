from dotenv import load_dotenv
from flask import Flask
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from os import getenv
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from wtforms import SubmitField
from wtforms.validators import DataRequired

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = getenv("SECRET_KEY")
app.config["MAX_CONTENT_LENGTH"] = 2 * 1024 * 1024 # makes sure file is not larger than 2MB

class ZipUploadForm(FlaskForm):
    file = FileField('file', validators=[DataRequired()])
    submit = SubmitField('submit')

# credentials for spotify dev acc (make this more secure later)
spotify = Spotify(auth_manager=SpotifyClientCredentials(
    client_id=getenv("SPOTIFY_CLIENT_ID"),
    client_secret=getenv("SPOTIFY_CLIENT_SECRET")
))

from app import views

if __name__ == "__main__":
    app.debug = True