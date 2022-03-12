from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, AnyOf, URL, NumberRange

class PetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired(message='Name cannot be blank')])
    species = SelectField("Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
    photo_url = StringField("Photo URL")
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    note = TextAreaField("Notes")
    
class EditPetForm(FlaskForm):
    photo_url = StringField("Photo URL")
    note = TextAreaField("Notes")
    available = BooleanField("Available?")