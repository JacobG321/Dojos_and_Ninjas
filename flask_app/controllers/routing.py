
from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.dojos import Dojos
from flask_app.models.ninjas import Ninjas
#import class models here

#home
@app.route('/dojos')
def index():
    dojos = Dojos.get_all()
    print(dojos)
    return render_template('index.html', all_dojos = dojos)

#takes use to the add ninjas page
@app.route('/add_ninjas')
def add_ninjas():
    dojos = Dojos.get_all()
    print(dojos)
    return render_template('add_ninja.html', all_dojos = dojos)

#views all ninjas at dojo
@app.route('/dojos/<int:id>')
def view_dojo(id):
    data = {
        'id': id
    }
    return render_template('dojo_view.html', this_dojo = Dojos.get_all_ninjas_from_dojo(data))



#invisible routes

#creates a new dojo
@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    data = {
        'dojo_name': request.form['dojo_name']
    }
    Dojos.save(data)
    return redirect('/dojos')

@app.route('/create_ninja', methods=['POST'])
def create_ninja():
    data = {
        'dojo_id': request.form['dojo_id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age']
    }
    id = data['dojo_id']
    Ninjas.save(data)
    return redirect(f'/dojos/{id}')



#when I add a ninja it says url not found
#Name of dojo not displaying on page when loaded