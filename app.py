from flask import Flask, render_template, redirect, url_for
from config import app
from routes.cliente_routes import cliente_bp
from routes.producto_routes import producto_bp

# Registrar blueprints
app.register_blueprint(cliente_bp)
app.register_blueprint(producto_bp)

@app.route('/')
def index():
    """Página principal"""
    return render_template('base.html', titulo='Bienvenido')


if __name__ == '__main__':
    app.run(debug=True)