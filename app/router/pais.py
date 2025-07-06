from fastapi import APIRouter, Depends, HTTPException
from ..db import get_db
from ..crud.pais import create_pais, get_pais_id, update_pais_id, delete_pais
from sqlalchemy.orm import Session, session
from typing import Optional
from datetime import date

from app.crud import pais

router = APIRouter()


@router.post("/")
def create_pais_endpoint(
    nombre: str,
    session: Session = Depends(get_db),
):
    pais = create_pais(session, nombre)
    return {
        "id": pais.id,
        "nombre": pais.nombre,
    }


@router.get("/{pais_id}")
def get_pais_id_endpoint(
    pais_id: int,
    session: Session = Depends(get_db),
):
    pais = get_pais_id(session, pais_id)
    if not pais:
        raise HTTPException(status_code=404, detail="Pais no encontrado")
    return {
        "id": pais.id,
        "nombre": pais.nombre,
    }


@router.put("/(pais_id)")
def update_pais_id_endpoint(
    pais_id: int,
    nombre: Optional[str] = None,
    session: Session = Depends(get_db),
):
    pais = update_pais_id(session, pais_id, nombre)
    if not pais:
        raise HTTPException(status_code=404, detail="Genero no encontrado")
    return {
        "id": pais.id,
        "nombre": pais.nombre,
    }


@router.delete("/{pais_id}")
def delete_pais_endpoint(pais_id: int, session: Session = Depends(get_db)):
    pais = delete_pais(session, pais_id)
    if not pais:
        raise HTTPException(status_code=404, detail="Genero no encontrado")
    return {
        "id": pais.id,
        "nombre": pais.nombre,
    }
