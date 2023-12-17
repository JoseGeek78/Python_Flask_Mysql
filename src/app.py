from flask import Flask, render_template
import os


template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')

app = Flask(__name__, template_folder = template_dir)


# Rutas de la aplicación
@app.route('/')
def home():
    cursor = db.database.cursor()
    cursor.execute('SELECT * FROM users')
    myresult = cursor.fetchall()
    # Convertir los datos a diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.appen(dict(zip(columnNames, record)))
    cursor.colse()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=4000)
    
   