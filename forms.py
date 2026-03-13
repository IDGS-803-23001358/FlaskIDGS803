##CLASE forms
from wtforms import Form, SelectField, TextAreaField
from wtforms import Form
from wtforms import StringField, IntegerField,PasswordField
from wtforms import EmailField
from wtforms import validators
from wtforms import RadioField

class Userform(Form):
     id=IntegerField('Matricula',[
     validators.DataRequired(message='El campo es requerido'),
     validators.NumberRange(min=2,max=100, message='ingresa valor valido') 
     ])  
     nombre=StringField('Nombre',[
     validators.DataRequired(message='El campo es requerido'),
     validators.length(min=4, max=10, message='ingrese nombre valido')])
     apellidos=StringField('apellidos',[
     validators.DataRequired(message='El campo es requerido')])
     telefono=StringField('telefono',[
     validators.DataRequired(message='El campo es requerido')])
     email=EmailField('correo',[
     validators.DataRequired(message='El campo es requerido')])
class MaestroForm(Form):
    matricula = IntegerField('Matricula', [
        validators.DataRequired()
    ])

    nombre = StringField('Nombre', [
        validators.DataRequired()
    ])

    apellidos = StringField('Apellidos', [
        validators.DataRequired()
    ])

    especialidad = StringField('Especialidad', [
        validators.DataRequired()
    ])

    email = EmailField('Correo', [
        validators.DataRequired()
    ])
class CursoForm(Form):
    id=IntegerField("id")
    nombre=StringField("Nombre",[
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=4, max=10, message="Ingrese nombre valido")
        ])

    descripcion = TextAreaField('Descripción', [
        validators.DataRequired()
    ])
    
    maestro = SelectField("Maestro", coerce=int)    