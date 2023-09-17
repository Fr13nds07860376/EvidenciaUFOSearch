from flask import Flask, render_template, request
from googlesearch import search
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar', methods=['POST'])
def buscar():
    google_query = request.form['query']
    
    # Realiza una búsqueda de Google
    resultados = []
    for i, result in enumerate(search(google_query, num=20, stop=20, pause=2), 1):
        resultados.append({'title': result, 'link': result})

    # Término de búsqueda con palabras clave de evidencia
    QUERY = 'vida extraterrestre evidencia "ovnis" "UAP" "objeto no identificado" "Top Secret" "Confidencial" "Ultrasecreto" "documentos "declassified" "unclassified" pdf" "Classified" "U.S. Air Force"'
    palabras_clave_evidencia = ["foto", "video", "documento"]

    # Número de resultados a buscar
    NUM_RESULTS = 133000

    # Realiza la búsqueda en Google
    results = list(search(QUERY, num=NUM_RESULTS, stop=NUM_RESULTS, pause=2))

    # Muestra los títulos y enlaces de los resultados en un formato de lista
    for i, result in enumerate(results, 1):
        resultados.append({'title': result, 'link': result})

    # Búsqueda adicional usando 'requests'
    agencias_gobierno = ["Fuerza Aérea de los Estados Unidos"]
    informes_ovnis = []

    for agencia in agencias_gobierno:
        search_query = f"{agencia} informes ovnis Classified"
        url = f"https://www.google.com/search?q={search_query}"
        response = requests.get(url)

        # Procesa la respuesta de la búsqueda 'requests' si es necesario
        # (esto puede implicar raspar datos de la página o analizar el contenido de la respuesta)
        
        informes_ovnis.append(response.url)  # Agrega la URL de la búsqueda a la lista de informes_ovnis

    # Imprime las URLs de los informes de ovnis encontrados
    for i, url in enumerate(informes_ovnis, 1):
        resultados.append({'title': f"Informe de OVNIs {i}", 'link': url})

    return render_template('index.html', resultados=resultados)

if __name__ == '__main__':
    app.run(debug=True)
