from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__)
app.secret_key = 'daadad'

# Configuración de MongoDB Atlas
MONGO_URI = "mongodb+srv://gerardohp93:DHkkwBpyT7yqimk2@cluster0.ohkgl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Nota: Reemplaza <usuario> y <contraseña> con tus credenciales reales

# Función para obtener la conexión a MongoDB
def get_db():
    client = MongoClient(MONGO_URI)
    return client.tienda_db