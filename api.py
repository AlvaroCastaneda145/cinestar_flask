from flask import Flask
import mysql.connector

config = {
    'host' : 'localhost',
    'user' : 'root',
    'password' : '',
    'database' : 'cinestar'      
}

configRemote={
    'host' : 'srv1101.hstgr.io',
    'user' : 'u584908256_cinestar',
    'password' : 'Senati2023@',
    'database' : 'u584908256_cinestar'  
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()
app = Flask(__name__)

@app.route("/cines")
def cines():
    cursor.execute('call sp_getCines()')
    cines = cursor.fetchall()
    cursor.close()
    return cines

@app.route("/peliculas/<id>")
def peliculas_cartelera(id):
    return "Hola id"

@app.route("/peliculas/<int:id>")
def peliculas_cartelera(id):
    return "int id"

# @app.route("/peliculas/cartelera")
# def peliculas_cartelera():
#     return"Cartelera"

@app.route("/peliculas/estrenos")
def peliculas_estrenos():
    return"Estrenos"


if __name__ == '__main__' :
    app.run(debug=True, port=5000)

    

    
