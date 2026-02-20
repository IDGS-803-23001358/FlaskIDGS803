##CLASE forms
from wtforms import Form
from wtforms import StringField, IntegerField,PasswordField
from wtforms import EmailField
from wtforms import validators
from wtforms import RadioField

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField
from wtforms import validators

class Userform(FlaskForm):

    id = IntegerField('Matricula', [
        validators.DataRequired(message='El campo es requerido'),
        validators.NumberRange(min=2, max=100, message='Ingresa valor válido')
    ])

    nombre = StringField('Nombre', [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=10, message='Ingrese nombre válido')
    ])

    apaterno = StringField('Apaterno', [
        validators.DataRequired(message='El campo es requerido')
    ])

    email = EmailField('Correo', [
        validators.DataRequired(message='El campo es requerido')
    ])
