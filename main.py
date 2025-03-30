from fastapi import FastAPI
import os

# Ruta donde están las bases de datos
DBS_DIR = r"C:\Users\MalwareTech\Desktop\dbs\dbs"

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API de bases de datos activa"}

@app.get("/list_dbs/")
def list_dbs():
    """Lista todas las bases de datos en la carpeta."""
    try:
        files = os.listdir(DBS_DIR)
        return {"databases": files}
    except Exception as e:
        return {"error": str(e)}

@app.get("/read_db/{filename}")
def read_db(filename: str):
    """Lee el contenido de una base de datos específica."""
    file_path = os.path.join(DBS_DIR, filename)

    if not os.path.exists(file_path):
        return {"error": "Archivo no encontrado"}

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return {"filename": filename, "content": content}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
