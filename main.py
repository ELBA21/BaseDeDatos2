
import logging

from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

from .app.router import asociacion,partido, el_set, torneo,mesa,fase,categoria,jugador,equipo


@asynccontextmanager
async def lifespan(_: FastAPI):
    # Inicio de la aplicación
    logging.info("Aplicación iniciada")

    yield

    # Cierre de la aplicación
    logging.info("Aplicación cerrada")
    pass


FASTAPI_CONFIG = {
    "title": "Aplicación FastAPI",
    "description": "Una aplicación de ejemplo utilizando FastAPI",
    "openapi_url": "/openapi.json",
    "version": "0.1.0",
    "swagger_ui_parameters": {"defaultModelsExpandDepth": -1},
}

MIDDLEWARE_CONFIG = {
    "allow_origins": ["*"],
    "allow_credentials": True,
    "allow_methods": ["*"],
    "allow_headers": ["*"],
}  # Permite solicitudes desde cualquier origen

app = FastAPI(**FASTAPI_CONFIG, lifespan=lifespan)
app.add_middleware(CORSMiddleware, **MIDDLEWARE_CONFIG)

# Routers
app.include_router(asociacion.router, prefix="/Asociacion", tags=["asociacion"])
app.include_router(partido.router, prefix="/Partido", tags=["partido"])
app.include_router(el_set.router,prefix="/Set",tags=["Set"])
app.include_router(torneo.router,prefix="/Torneo", tags=["torneo"])
app.include_router(mesa.router, prefix="/Mesa", tags=["mesa"])
app.include_router(fase.router, prefix="/Fase", tags=["fase"])
app.include_router(categoria.router, prefix="/Categoria", tags=["categoria"])
app.include_router(jugador.router, prefix="/Jugador", tags=["jugador"])
app.include_router(equipo.router, prefix="/Equipo", tags=["equipo"])