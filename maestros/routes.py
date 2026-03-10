
from . import maestros

from models import db
from models import Alumnos, Maestros

from flask import render_template, request, redirect, url_for
from . import maestros
from models import db, Maestros
import forms
from forms import MaestroForm



@maestros.route("/maestros", methods=['GET','POST'])
def maestros_index():

    create_form = MaestroForm(request.form)
    maestros_lista = Maestros.query.all()

    return render_template(
        "index1.html",
        form=create_form,
        maestros=maestros_lista
    )


# CREAR
@maestros.route('/maestros/crear', methods=['GET', 'POST'])
def crear():
    form = MaestroForm(request.form)

    if request.method == 'POST':
        maestro = Maestros(
            matricula=form.matricula.data,
            nombre=form.nombre.data,
            apellidos=form.apellidos.data,
            especialidad=form.especialidad.data,
            email=form.email.data
        )
        db.session.add(maestro)
        db.session.commit()
        return redirect(url_for('maestros.maestros_index'))

    return render_template('maestros.html', form=form)



@maestros.route('/maestros/detalles/<int:matricula>')
def detalles(matricula):
    maestro = Maestros.query.get(matricula)
    return render_template('detalles1.html', maestro=maestro)


# MODIFICAR
@maestros.route('/maestros/modificar/<int:matricula>', methods=['GET','POST'])
def modificar(matricula):
    maestro = Maestros.query.get(matricula)
    form = MaestroForm(request.form, obj=maestro)

    if request.method == 'POST':
        maestro.nombre = form.nombre.data
        maestro.apellidos = form.apellidos.data
        maestro.especialidad = form.especialidad.data
        maestro.email = form.email.data

        db.session.commit()
        return redirect(url_for('maestros.maestros_index'))

    return render_template('modificar1.html', form=form)


from forms import MaestroForm

# ELIMINAR
@maestros.route('/maestros/eliminar/<int:matricula>', methods=['GET','POST'])
def eliminar(matricula):

    maestro = Maestros.query.get(matricula)
    form = MaestroForm(obj=maestro)

    if request.method == 'POST':
        db.session.delete(maestro)
        db.session.commit()
        return redirect(url_for('maestros.maestros_index'))

    return render_template('eliminar1.html', form=form, maestro=maestro)


@maestros.route('/perfil/<nombre>')
def perfil(nombre):
    return f"Perfil de {nombre}"