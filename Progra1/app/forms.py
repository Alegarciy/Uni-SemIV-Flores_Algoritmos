# Generates html forms using python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_wtf.file import FileField, FileAllowed

# New form datatype
class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
                                    validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sing_Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class ImageForm(FlaskForm):
    image_01 = FileField('Upload flower #1', validators=[DataRequired(), FileAllowed(['png'])])
    image_02 = FileField('Upload flower #2', validators=[DataRequired(), FileAllowed(['png'])])
    image_03 = FileField('Upload flower #3', validators=[FileAllowed(['png'])])
    json = FileField("Upload JSON", validators=[FileAllowed(['txt'])])
    submit = SubmitField('Upload')
    submit_02 = SubmitField('pruebita') 