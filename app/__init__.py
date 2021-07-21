from flask import Flask
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from wtforms import SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
# change this to something more secure later lmao
app.config["SECRET_KEY"] = "fZYidiMjTU@Qg&J*@QM6mnpNjEcXChqP@KjCkz!5fcyMarb4H*57yGRWYP@U4Pn#"
app.config["MAX_CONTENT_LENGTH"] = 2 * 1024 * 1024 # makes sure file is not larger than 2MB
class ZipUploadForm(FlaskForm):
    file = FileField('file', validators=[DataRequired()])
    submit = SubmitField('submit')

# credentials for spotify dev acc (make this more secure later)
spotify = Spotify(auth_manager=SpotifyClientCredentials(
    client_id="5d0448251c3e422eb0a97bf0852db996",
    client_secret="16f9c54d622c422fb3523e3b06b635d6"
))

from app import views

if __name__ == "__main__":
    app.debug = True