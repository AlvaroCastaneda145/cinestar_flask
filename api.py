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

app = Flask(__name__)

@app.route("/cines")
def index():
    return"Cines"

if __name__ == '__main__' :
    app.run(debug=True)

    