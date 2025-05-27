from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from routers import todos  # Descomenta esta línea cuando tengas el archivo routers/todos.py
import config

app = FastAPI()
# app.include_router(todos.router)  # Descomenta esta línea cuando tengas el archivo routers/todos.py

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.get("/")
# def read_root():
#     return "Hello World"

# @app.get("/")
# def read_root():
#     print("Entrando a read_root")  # Log en consola
#     return {"message": "Hello World"}

# @app.get("/todos")
# def get_todos():
#     return db.query(Todo).all()

@app.get("/todos")
def get_todos():
    return [
        {"id": 1, "name": "Tarea de ejemplo", "completed": False},
        {"id": 2, "name": "Otra tarea", "completed": True}
    ]