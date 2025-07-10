from fastapi import APIRouter, Depends, HTTPException

from ..models import Genero
from ..db import get_db
from ..crud.genero import create_genero, get_genero_id, update_genero_id, delete_genero
from sqlalchemy.orm import Session, session
from typing import Optional
from datetime import date

router = APIRouter()


@router.post("/")
def create_genero_endpoint(
    nombre: str,
    session: Session = Depends(get_db),
):
    duplicado = session.query(Genero).filter_by(nombre=nombre).first()
    if duplicado:
        raise HTTPException(status_code=400, detail="Genero ya existente")
    # Esto se haria en el models.py poniendole unique al nombre pero ya es muy tarde para andar editando el models.py y hacer una migracion

    genero = create_genero(session, nombre)
    return {
        "id": genero.id,
        "nombre": genero.nombre,
    }


@router.get("/{genero_id}")
def get_genero_id_endpoint(
    genero_id: int,
    session: Session = Depends(get_db),
):
    genero = get_genero_id(session, genero_id)
    if not genero:
        raise HTTPException(status_code=404, detail="Genero no encontrado")
    return {
        "id": genero.id,
        "nombre": genero.nombre,
    }


@router.put("/{genero_id}")
def update_genero_id_endpoint(
    genero_id: int,
    nombre: Optional[str] = None,
    session: Session = Depends(get_db),
):
    if nombre is not None:
        duplicado = session.query(Genero).filter_by(nombre=nombre).first()
        if duplicado:
            raise HTTPException(status_code=400, detail="Genero ya existente")
    genero = update_genero_id(session, genero_id, nombre)
    if not genero:
        raise HTTPException(status_code=404, detail="Genero no encontrado")
    return {
        "id": genero.id,
        "nombre": genero.nombre,
    }


@router.delete("/{genero_id}")
def delete_genero_endpoint(genero_id: int, session: Session = Depends(get_db)):
    genero = delete_genero(session, genero_id)
    if not genero:
        raise HTTPException(status_code=404, detail="Genero no encontrado")
    return {
        "id": genero.id,
        "nombre": genero.nombre,
    }
