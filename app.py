from flask import Flask

# Inicializamos la aplicación Flask
app = Flask(__name__)

# Ruta principal
@app.route('/')
def home():
    return "¡Hola! Flask está funcionando correctamente "

# Ruta personalizada con nombre de usuario
@app.route('/usuario/<nombre>')
def usuario(nombre):
    return f"Bienvenido Proyecto Flask, {nombre}"

# Punto de entrada
if __name__ == '__main__':
    app.run(debug=True)
