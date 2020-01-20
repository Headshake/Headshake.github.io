from flask import Flask
from flask import render_template
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/about.html', methods=['GET'])   
def about():
    return render_template('about.html')

@app.route('/menu.html', methods=['GET'])   
def take():
    return render_template('menu.html')

@app.route('/reservation.html', methods=['GET'])   
def give():
    return render_template('reservation.html')

@app.route('/contact.html', methods=['GET'])   
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug = True)
    database = sqlite3.connect('database.db')
    print("Opened database successfully")

    database.execute('CREATE TABLE partners (name TEXT, phone INTEGER, email TEXT, addr TEXT, leftover TEXT, price REAL)')
    print("Database created successfully")
    database.close()