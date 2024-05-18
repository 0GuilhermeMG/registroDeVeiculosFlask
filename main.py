from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

def save_vehicle(data):
    with open('vehicles.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def load_vehicles():
    vehicles = []
    with open('vehicles.csv', mode='r') as file:
        reader = csv.reader(file)
        vehicles = list(reader)
    return vehicles

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        make = request.form['make']
        model = request.form['model']
        year = request.form['year']
        placa = request.form['placa']
        data = [make, model, year, placa]
        save_vehicle(data)
        return redirect(url_for('list_vehicles'))
    return render_template('register.html')

@app.route('/list')
def list_vehicles():
    vehicles = load_vehicles()
    return render_template('list.html', vehicles=vehicles)

if __name__ == '__main__':
    app.run(debug=True)
