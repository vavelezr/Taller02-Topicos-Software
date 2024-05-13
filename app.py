from flask import Flask, jsonify, render_template, url_for
import random
import json
import os 

app = Flask(__name__)

def cargar_pokeneas():
    with open('data/pokeneas.json', 'r') as archivo:
        pokeneas = json.load(archivo)
    return pokeneas

pokeneas = cargar_pokeneas()

@app.route('/')
def index():
    return render_template('base.html')    
    

@app.route('/api/pokenea')
def api_pokenea():
    pokenea = random.choice(pokeneas)
    pokenea['id_contenedor'] = os.uname()[1]
    return render_template('filosofico.html',pokenea=pokenea)


@app.route('/pokeneas')
def show_pokeneas():
    pokenea = random.choice(pokeneas)
    pokenea['id_contenedor'] = os.uname()[1]
    return render_template('pokenea.html',pokenea=pokenea)


@app.route('/pokeneas/json')
def show_pokenea_json():
    pokenea = random.choice(pokeneas)
    pokenea['id_contenedor'] = os.uname()[1]
    data = {
        'id': pokenea['id'],
        'nombre': pokenea['nombre'],
        'altura': pokenea['altura'],
        'habilidad': pokenea['habilidad'],
        #'id_contenedor': pokenea['id_contenedor'],
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)