from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

app = Flask(__name__)

# Cargar el modelo RandomForestRegressor
model = joblib.load('modelo_rf.joblib')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    year = None
    if request.method == 'POST':
        # Obtener los valores ingresados por el usuario
        year = int(request.form['year'])
        new_data = {
            'Año': [year],
            'Temperatura': [float(request.form['temperature'])],
            'Precipitacion': [float(request.form['precipitation'])],
            'Riego adecuado (7 Dias)': [int(request.form['irrigation'])],
            'Gestion de plagas': [int(request.form['pest_management'])],
            'Densidad (ha2)': [int(request.form['density'])],
            'Espaciado entre planta (cm)': [int(request.form['plant_spacing'])],
            'Analisis de suelo (pH)': [float(request.form['soil_analysis'])],
            'Profundidad de siembra de planta (cm)': [int(request.form['planting_depth'])]
        }

        new_data = pd.DataFrame(new_data)

        # Realizar la predicción
        y_pred_new = model.predict(new_data)

        # Mostrar la predicción
        prediction = round(y_pred_new[0])

    # Renderizar la plantilla HTML con el formulario y los resultados
    return render_template('index.html', prediction=prediction, year=year)

if __name__ == '__main__':
    app.run(debug=True)
