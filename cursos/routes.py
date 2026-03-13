
from . import cursos

from models import db
from models import Cursos, Maestros

from flask import render_template, request, redirect, url_for
from . import cursos
from models import db, Cursos
import forms
from forms import CursoForm


@cursos.route('/cursos')
def cursos_index():

    cursos_lista = Cursos.query.all()

    return render_template(
        'index2.html',
        cursos=cursos_lista
    )
@cursos.route('/cursos/agregar', methods=['GET','POST'])
def agregar():

    form = CursoForm(request.form)

    if request.method == 'POST':

        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        maestro_id = request.form['maestro']

        nuevo = Cursos(
            nombre=nombre,
            descripcion=descripcion,
            maestro_id=maestro_id
        )

        db.session.add(nuevo)
        db.session.commit()

        return redirect(url_for('cursos.cursos_index'))

    maestros = Maestros.query.all()

    return render_template(
        'cursos.html',
        form=form,
        maestros=maestros
    )
@cursos.route('/cursos/detalles')
def detalles():

    id = request.args.get('id')

    curso = Cursos.query.filter(Cursos.id == id).first()

    return render_template(
        'detalles2.html',
        curso=curso
    )
@cursos.route('/cursos/modificar', methods=['GET','POST'])
def modificar():

    form = CursoForm(request.form)

    maestros = Maestros.query.all()

    if request.method == 'GET':

        id = request.args.get('id')

        curso = Cursos.query.filter(Cursos.id == id).first()

        form.id.data = curso.id
        form.nombre.data = curso.nombre
        form.descripcion.data = curso.descripcion
        form.maestro.data = curso.maestro_id

        return render_template(
            'modificar2.html',
            form=form,
            maestros=maestros,
            curso=curso
        )

    if request.method == 'POST':

        id = form.id.data

        curso = Cursos.query.filter(Cursos.id == id).first()

        curso.nombre = form.nombre.data
        curso.descripcion = form.descripcion.data
        curso.maestro_id = request.form['maestro']

        db.session.commit()

        return redirect(url_for('cursos.cursos_index'))
@cursos.route('/cursos/eliminar', methods=['GET','POST'])
def eliminar():

    form = CursoForm(request.form)

    maestros = Maestros.query.all()

    if request.method == 'GET':

        id = request.args.get('id')

        curso = Cursos.query.filter(Cursos.id == id).first()

        form.id.data = curso.id
        form.nombre.data = curso.nombre
        form.descripcion.data = curso.descripcion
        form.maestro.data = curso.maestro_id

        return render_template(
            'eliminar2.html',
            form=form,
            curso=curso,
            maestros=maestros
        )

    if request.method == 'POST':

        id = form.id.data

        curso = Cursos.query.filter(Cursos.id == id).first()

        db.session.delete(curso)
        db.session.commit()

        return redirect(url_for('cursos.cursos_index'))
    