from fastapi  import APIRouter, Depends, HTTPException
from ..db import get_db
from ..crud.asociacion import (get_asociacion_all, create_asociacion, update_asociacion_all, delete_asociacion)
from sqlalchemy.orm import Session
router = APIRouter()


@router.post("/")
def create_asociacion_endpoint(nombre: str, ciudad: str, pais: str, session: Session = Depends(get_db)):
    asociacion = create_asociacion(session, nombre, ciudad, pais)
    return {"id": asociacion.id, "nombre": asociacion.nombre, "ciudad": asociacion.ciudad, "pais": asociacion.pais}

@router.get("/")
def get_asociaciones_all_endpoint(session: Session = Depends(get_db)):
    asociaciones = get_asociacion_all(session)
    return [{"id": asociacion.id, "nombre": asociacion.nombre, "ciudad": asociacion.ciudad, "pais": asociacion.pais} for asociacion in asociaciones]


