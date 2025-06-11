from fastapi import FastAPI, Depends
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware
from functools import lru_cache

from typing import Union

# routers: comment out next line till create them
from routers import todos

import config

app = FastAPI()

# router: comment out next line till create it
app.include_router(todos.router)


origins = [
    "http://localhost:3000",
    "https://todo-frontend-khaki.vercel.app",
]

# CORS configuration, needed for frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.get("/")
# def read_root():
#     return {"message": "API funcionando correctamente"}






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


# global http exception handler, to handle errors
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    print(f"{repr(exc)}")
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

# to use the settings
@lru_cache()
def get_settings():
    return config.Settings()


@app.get("/")
def read_root(settings: config.Settings = Depends(get_settings)):
    # print the app_name configuration
    print(settings.APP_NAME)
    return "Hello World"


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
