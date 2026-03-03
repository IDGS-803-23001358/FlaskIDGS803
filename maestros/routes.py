
from . import maestros



@maestros.route('/perfil/<nombre>')
def perfil(nombre):
    return f"Perfil de {nombre}"