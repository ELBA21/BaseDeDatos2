from fastapi  import APIRouter, Depends, HTTPException
from ..db import get_db
from ..crud.asociacion import (get_asociacion_id, create_asociacion, update_asociacion_id, delete_asociacion)
from sqlalchemy.orm import Session
from typing import Optional
router = APIRouter()


@router.post("/")
def create_asociacion_endpoint(nombre: str, ciudad: str, pais: str, session: Session = Depends(get_db)):
    asociacion = create_asociacion(session, nombre, ciudad, pais)
    return {"id": asociacion.id, "nombre": asociacion.nombre, "ciudad": asociacion.ciudad, "pais": asociacion.pais}

@router.get("/{asociacion_id}")
def get_asociacion_id_endpoint(asociacion_id:int, session: Session = Depends(get_db)):
    asociacion = get_asociacion_id(session,asociacion_id)
    return {"id": asociacion.id, "nombre": asociacion.nombre, "ciudad": asociacion.ciudad, "pais": asociacion.pais}

@router.put("/{asociacion_id}")
def update_asociacion_id_endpoint(asociacion_id:int, nombre:Optional[str]=None, ciudad: Optional[str]=None, pais:Optional[str]=None, session: Session = Depends(get_db)):
    asociacion = update_asociacion_id(session,asociacion_id,nombre, ciudad,pais)
    return {"id": asociacion_id, "nombre": asociacion.nombre, "ciudad": asociacion.ciudad, "pais": asociacion.pais}

@router.delete("/{asociacion_id}")
def delete_asociacion_endpoint(asociacion_id:int, session: Session = Depends(get_db)):
    asociacion = delete_asociacion(session, asociacion_id)
    if not asociacion:
        raise HTTPException(status_code=404,detail="Asociacion no encontrada")
    return {"detail", asociacion.id}