from fastapi  import APIRouter, Depends, HTTPException
from ..db import get_db
from ..crud.torneo import (create_torneo, get_torneo_id, update_torneo_id, delete_torneo_id)
from sqlalchemy.orm import Session
from typing import Optional
from datetime import date
router = APIRouter()

@router.post("/")
def create_torneo_endpoint(nombre:str, fecha_Inscripcion:date, competencia:str, session: Session = Depends(get_db)):
    torneo = create_torneo(session, nombre, fecha_Inscripcion, competencia)
    return {"nombre": torneo.nombre, "fecha_inscripcion": torneo.fecha_Inscripcion, "competencia": torneo.competencia}

@router.get("/{torneo_id}")
def get_torneo_id_endpoint(torneo_id:int, session:Session= Depends(get_db)):
    torneo = get_torneo_id(session, torneo_id)
    return {"id": torneo.id, "nombre": torneo.nombre, "fecha_inscripcion": torneo.fecha_Inscripcion, "competencia": torneo.competencia}
    
@router.put("/{torneo_id}")
def update_torneo_id_endpoint(torneo_id:int, nombre:Optional[str] = None, fecha_Inscripcion:Optional[date] = None, competencia:Optional[str] = None, session:Session=Depends(get_db)):
    torneo = update_torneo_id(session, torneo_id, nombre, fecha_Inscripcion, competencia)
    return {"id": torneo.id, "nombre": torneo.nombre, "fecha_inscripcion": torneo.fecha_Inscripcion, "competencia": torneo.competencia}

@router.delete("/{torneo_id}")
def delete_torneo_id_endpoint(torneo_id:int, session:Session=Depends(get_db)):
    torneo = delete_torneo_id(session,torneo_id)
    return {"id": torneo.id, "nombre": torneo.nombre, "fecha_inscripcion": torneo.fecha_Inscripcion, "competencia": torneo.competencia}