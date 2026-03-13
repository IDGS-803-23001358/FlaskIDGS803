
from . import inscripciones
from flask import render_template, request, redirect, url_for
from models import db, Alumnos, Cursos, Inscripciones


@inscripciones.route('/inscripciones')
def lista():

    inscripciones = Inscripciones.query.all()

    return render_template(
        "index3.html",
        inscripciones=inscripciones
    )


@inscripciones.route('/inscripciones/agregar', methods=['GET','POST'])
def agregar():

    if request.method == 'POST':

        alumno_id = request.form['alumno']
        curso_id = request.form['curso']

        alumno = Alumnos.query.get(alumno_id)
        curso = Cursos.query.get(curso_id)

        # relación muchos a muchos
        curso.alumnos.append(alumno)

        db.session.commit()

        return redirect(url_for('inscripciones.lista'))

    alumnos = Alumnos.query.all()
    cursos = Cursos.query.all()

    return render_template(
        "inscripciones.html",
        alumnos=alumnos,
        cursos=cursos
    )


@inscripciones.route('/inscripciones/detalles')
def detalles():

    id = request.args.get('id')

    inscripcion = Inscripciones.query.get(id)

    return render_template(
        "detalles3.html",
        inscripcion=inscripcion
    )


@inscripciones.route('/inscripciones/modificar', methods=['GET','POST'])
def modificar():

    if request.method == 'GET':

        id = request.args.get('id')

        inscripcion = Inscripciones.query.get(id)

        alumnos = Alumnos.query.all()
        cursos = Cursos.query.all()

        return render_template(
            "modificar3.html",
            inscripcion=inscripcion,
            alumnos=alumnos,
            cursos=cursos
        )


    if request.method == 'POST':

        id = request.form['id']
        alumno_id = request.form['alumno']
        curso_id = request.form['curso']

        inscripcion = Inscripciones.query.get(id)

        inscripcion.alumno_id = alumno_id
        inscripcion.curso_id = curso_id

        db.session.commit()

        return redirect(url_for('inscripciones.lista'))


@inscripciones.route('/inscripciones/eliminar', methods=['GET','POST'])
def eliminar():

    if request.method == 'GET':

        id = request.args.get('id')

        inscripcion = Inscripciones.query.get(id)

        alumnos = Alumnos.query.all()
        cursos = Cursos.query.all()

        return render_template(
            "eliminar3.html",
            inscripcion=inscripcion,
            alumnos=alumnos,
            cursos=cursos
        )

    if request.method == 'POST':

        id = request.form['id']

        inscripcion = Inscripciones.query.get(id)

        db.session.delete(inscripcion)

        db.session.commit()

        return redirect(url_for('inscripciones.lista'))