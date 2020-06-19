# Generates html forms using python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_wtf.file import FileField, FileAllowed

class ImageForm(FlaskForm):
    image = FileField('Upload flower image', validators=[DataRequired(), FileAllowed(['png'])])
    json = FileField("Upload JSON", validators=[DataRequired(), FileAllowed(['txt'])])
    submit = SubmitField('Upload')
