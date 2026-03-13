
from . import alumnos

from models import db
from models import Alumnos, Maestros

from flask import render_template, request, redirect, url_for
from . import alumnos
from models import db, Alumnos
import forms
from forms import Userform


@alumnos.route("/index")
def index():
    create_form = forms.Userform(request.form)
    alumno = Alumnos.query.all()

    return render_template(
        "index.html",
        form=create_form,
        alumno=alumno
    )


@alumnos.route("/alumnos", methods=['GET', 'POST'])
def alumnos_view():

    create_form = forms.Userform(request.form)

    if request.method == 'POST':

        alum = Alumnos(
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            email=create_form.email.data,
            telefono=create_form.telefono.data
        )

        db.session.add(alum)
        db.session.commit()

        return redirect(url_for('alumnos.index'))

    return render_template("alumnos.html", form=create_form)


@alumnos.route("/detalles", methods=['GET', 'POST'])
def detalles():

    create_form = forms.Userform(request.form)

    if request.method == 'GET':

        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()

        nombre = alum1.nombre
        apellidos = alum1.apellidos
        telefono = alum1.telefono
        email = alum1.email

        return render_template(
            "detalles.html",
            nombre=nombre,
            apellidos=apellidos,
            email=email,
            telefono=telefono
        )


@alumnos.route("/modificar", methods=['GET', 'POST'])
def modificar():

    create_form = forms.Userform(request.form)

    if request.method == 'GET':

        id = request.args.get('id')

        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()

        create_form.id.data = id
        create_form.nombre.data = alum1.nombre
        create_form.apellidos.data = alum1.apellidos
        create_form.telefono.data = alum1.telefono
        create_form.email.data = alum1.email

    if request.method == 'POST':

        id = create_form.id.data

        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()

        alum1.nombre = create_form.nombre.data
        alum1.apellidos = create_form.apellidos.data
        alum1.email = create_form.email.data
        alum1.telefono = create_form.telefono.data

        db.session.add(alum1)
        db.session.commit()

        return redirect(url_for('alumnos.index'))

    return render_template("modificar.html", form=create_form)


@alumnos.route("/eliminar", methods=['GET', 'POST'])
def eliminar():

    create_form = forms.Userform(request.form)

    if request.method == 'GET':

        id = request.args.get('id')

        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()

        create_form.id.data = id
        create_form.nombre.data = alum1.nombre
        create_form.apellidos.data = alum1.apellidos
        create_form.telefono.data = alum1.telefono
        create_form.email.data = alum1.email

    if request.method == 'POST':

        id = request.args.get('id')

        alum = Alumnos.query.get(id)

        db.session.delete(alum)
        db.session.commit()

        return redirect(url_for('alumnos.index'))

    return render_template("eliminar.html", form=create_form)