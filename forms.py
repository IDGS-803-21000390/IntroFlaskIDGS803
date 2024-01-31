from wtforms import Form
from wtforms import StringField,SelectField,RadioField,EmailField,IntegerField


class UsarForm(Form):
    nombre=StringField('nombre')
    apaterno=StringField('apaterno')
    amaterno=StringField('amaterno')
    edad=IntegerField('edad')
    correo=EmailField('email')