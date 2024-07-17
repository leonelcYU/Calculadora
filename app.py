from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_interes', methods=['GET', 'POST'])
def calcular_interes():
    resultado = None
    if request.method == 'POST':
        try:
            monto = float(request.form['monto'])
            tasa = float(request.form['tasa'])
            tiempo = float(request.form['tiempo'])
            interes = monto * (tasa / 100) * tiempo
            total = monto + interes
            resultado = f"El interés es {interes:.2f} y el monto total a pagar es {total:.2f}."
        except ValueError:
            resultado = "Error: Asegúrate de ingresar números válidos."
    return render_template('calcular_interes.html', resultado=resultado)

@app.route('/dividir_terrenos', methods=['GET', 'POST'])
def dividir_terrenos():
    resultado = None
    if request.method == 'POST':
        try:
            metros = float(request.form['metros'])
            partes = int(request.form['partes'])
            resultado = f"Cada parte será de {metros / partes:.2f} metros cuadrados."
        except ValueError:
            resultado = "Error: Asegúrate de ingresar números válidos."
    return render_template('dividir_terrenos.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)







