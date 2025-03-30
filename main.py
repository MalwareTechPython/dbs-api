import requests
from fastapi import FastAPI

# URL de tu API local expuesta con Ngrok
NGROK_URL = "https://6111-190-173-58-152.ngrok-free.app"  

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API en Render funcionando"}

@app.get("/list_dbs/")
def list_dbs():
    """Solicita la lista de bases de datos desde la API local."""
    try:
        response = requests.get(f"{NGROK_URL}/list_dbs/")
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"No se pudo conectar a la API local: {str(e)}"}

@app.get("/read_db/{filename}")
def read_db(filename: str):
    """Solicita el contenido de un archivo de la base de datos."""
    try:
        response = requests.get(f"{NGROK_URL}/read_db/{filename}")
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"No se pudo conectar a la API local: {str(e)}"}

