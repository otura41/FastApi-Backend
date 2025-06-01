from fastapi import FastAPI, Depends
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware

# routers: comment out next line till create them
from routers import todos

import config

app = FastAPI()

# router: comment out next line till create it
app.include_router(todos.router)


origins = [
    "http://localhost:3000",
    "https://todo-frontend-khaki.vercel.app/",
]

# CORS configuration, needed for frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# # from routers import todos  # Descomenta esta línea cuando tengas el archivo routers/todos.py
# import config

# app = FastAPI()
# # app.include_router(todos.router)  # Descomenta esta línea cuando tengas el archivo routers/todos.py

# # Configuración CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

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

# @app.get("/todos")
# def get_todos():
#     return [
#         {"id": 1, "name": "Tarea de ejemplo", "completed": False},
#         {"id": 2, "name": "Otra tarea", "completed": True}
#     ]