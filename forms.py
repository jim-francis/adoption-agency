from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Optional

class AddPetForm(FlaskForm):
    name = StringField("Pet Name")
    species = StringField("Species")
    photo_url = StringField("Photo URL")
    age = IntegerField("Age")
    note = StringField("Notes")