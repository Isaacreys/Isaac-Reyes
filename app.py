from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.secret_key = 'your_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)

# Usuario de ejemplo
class User(UserMixin):
    def __init__(self, id):
        self.id = id

# Usuarios simulados
users = {'user@example.com': {'password': 'password'}}

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        if email in users and request.form['password'] == users[email]['password']:
            user = User(email)
            login_user(user)
            return redirect(url_for('home'))
        return 'Invalid credentials'
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# Definir rutas para todas las secciones
@app.route('/comparativa')
def comparativa():
    return render_template('comparativa.html')

@app.route('/recomendaciones')
def recomendaciones():
    return render_template('recomendaciones.html')

@app.route('/promociones')
def promociones():
    return render_template('promociones.html')

@app.route('/noticias')
def noticias():
    return render_template('noticias.html')

@app.route('/ayuda')
def ayuda():
    return render_template('ayuda.html')

if __name__ == '__main__':
    app.run(debug=True)

