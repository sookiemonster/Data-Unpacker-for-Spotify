from flask import Flask
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
# change this to something more secure later lmao
app.config["SECRET_KEY"] = "fZYidiMjTU@Qg&J*@QM6mnpNjEcXChqP@KjCkz!5fcyMarb4H*57yGRWYP@U4Pn#"
app.config["MAX_CONTENT_LENGTH"] = 2 * 1024 * 1024 # makes sure file is not larger than 2MB
class ZipUploadForm(FlaskForm):
    file = FileField('file', validators=[DataRequired()])
    submit = SubmitField('submit')

from app import views

if __name__ == "__main__":
    app.debug = True