from flask import Flask, render_template, request, redirect, url_for, flash
import requests
import json

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'una-clave-secreta-000001'

token = 'c1a5053fb8e289c5fd9b5931c5d721ddcf140300'
headers = {
        "Authorization": f"Token {token}",
        "Content-Type": "application/json"
    }

@app.route("/")
def hello_world():
    return "<p>Hola Mundo FLask Pa no sacar 0</p>"




@app.route("/los/edificios")
def los_edificios():
    """
    """
    r = requests.get("http://localhost:8000/api/edificios/",headers=headers)
    print("---------------------")
    print(r.content)
    print("---------------------")
    edificios = json.loads(r.content)['results']

    numero_edificios = json.loads(r.content)['count']
    return render_template("losEdificios.html", edificios=edificios,numero_edificios=numero_edificios)



@app.route("/los/despartamentos")
def los_departamentos():
    r = requests.get("http://localhost:8000/api/departamentos/", headers=headers)
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']

    for d in datos:
        d['edificio'] = obtener_Edificio(d['edificio'])

    return render_template("losDepartamentos.html", datos=datos, numero=numero)



# funciones ayuda

def obtener_Edificio(url):
    """
    http://127.0.0.1:8000/api/edificio/4/
    """
    r = requests.get(url, headers=headers)
    nombre_edificio = json.loads(r.content)['nombre']
   
    return nombre_edificio









@app.route("/crear_edificio", methods=['GET', 'POST'])
def agregar_edificio():
    """
    """
    if request.method == 'POST':
        

        nombre = request.form['nombre']
        app.logger.warning("Esto es una advertencia1")
        direccion = request.form['direccion']
        app.logger.warning("Esto es una advertencia2")
        ciudad = request.form['ciudad']
        app.logger.warning("Esto es una advertencia3")
        tipo = request.form['tipo']
        app.logger.warning("Esto es una advertencia4")
   

        # Datos a enviar a la API de Django
        edificio_data = {
            'nombre': nombre,
            'direccion': direccion,
            'ciudad': ciudad,
            'tipo': tipo
        }

        # Configuración de los headers para la autenticación por Token
        headers = {
            "Authorization": f"Token {token}",
            "Content-Type": "application/json"
        }
        app.logger.warning("Esto es una advertencia")
        app.logger.warning(edificio_data)

        # Realizar la petición POST a la API de Django
        r = requests.post("http://127.0.0.1:8000/api/edificios/",
                              json=edificio_data, # 'json' serializa el diccionario a JSON automáticamente
                              headers=headers)


        print(f"Status Code (Crear Edificio): {r.status_code}")
        # Si todo fue bien (código 201 Created), la API devuelve el objeto creado
        nuevo_edificio = json.loads(r.content)
        flash(f"edificio '{nuevo_edificio['nombre']} {nuevo_edificio['tipo']}' creado exitosamente!", 'success')
        return redirect(url_for('los_edificios')) # Redirigir a la lista de estudiantes


    return render_template("crearEdificio.html")







@app.route("/crear_depa", methods=['GET', 'POST'])
def agregar_depa():


    headers = {"Authorization": f"Token {token}","Content-Type": "application/json"}

    r_edificios = requests.get("http://localhost:8000/api/edificios/", headers=headers)
    edificios_disponibles = json.loads(r_edificios.content)['results']

    if request.method == 'POST':
        nombre_propietario = request.form['nombre_propietario']
        costo = request.form['costo']
        num_cuartos = request.form['num_cuartos']
        edificio_id = request.form['edificio'] 

        departamento_data = {
            'nombre_propietario': nombre_propietario,
            'costo': costo,
            'num_cuartos': num_cuartos,
            'edificio': edificio_id 
        }

        headers = {
            "Authorization": f"Token {token}",
            "Content-Type": "application/json"
        }

        app.logger.warning("Datos para crear departamento:")
        app.logger.warning(departamento_data)

        r = requests.post("http://127.0.0.1:8000/api/departamentos/",
                          json=departamento_data,
                          headers=headers)

        print(f"Status Code (Crear depa): {r.status_code}")
        if r.status_code == 201:
            nuevo_depa = json.loads(r.content)
            flash(f"Departamento '{nuevo_depa['nombre_propietario']}' creado exitosamente!", 'success')
            return redirect(url_for('los_departamentos'))
        else:
            flash(f"Error al crear departamento: {r.text}", 'danger')

    return render_template("crearDepa.html", edificios_disponibles=edificios_disponibles)









if __name__ == "__main__":
    app.run(debug=True)







#funcion ayuda pa luego#
