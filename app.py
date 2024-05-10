from flask import Flask, jsonify, render_template, url_for
import random
import json

app = Flask(__name__)




def get_container_id():
    try:
        # Leer la primera línea del archivo /proc/self/cgroup
        with open('/proc/self/cgroup', 'r') as file:
            first_line = file.readline()
        # Extraer el ID del contenedor de la línea
        # El formato generalmente es algo como "12:devices:/docker/93d...54b"
        return first_line.split('/')[-1].strip()
    except Exception as e:
        return f"Error al obtener el ID del contenedor: {e}"
    
# Carga los datos de los pokeneas desde un archivo JSON
def cargar_pokeneas():
    with open('data/pokeneas.json', 'r') as archivo:
        pokeneas = json.load(archivo)
    print(pokeneas)  # Esto imprimirá el contenido de pokeneas en la consola
    return pokeneas

pokeneas = cargar_pokeneas()

@app.route('/')
def index():
    return render_template('base.html')

    
    

#pokenea aleotario
@app.route('/api/pokenea')
def api_pokenea():
    pokenea = random.choice(pokeneas)
    return render_template('filosofico.html',pokenea=pokenea)


#Acá se muestra el pokenea
@app.route('/pokeneas')
def show_pokeneas():
    pokenea = random.choice(pokeneas)
    return render_template('pokenea.html',pokenea=pokenea)




if __name__ == '__main__':
    app.run(debug=True)