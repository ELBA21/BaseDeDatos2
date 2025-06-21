from fastapi  import APIRouter, Depends, HTTPException
from ..db import get_db
from ..crud.torneo import (create_torneo, get_torneo_id, update_torneo_id, delete_torneo_id)
from sqlalchemy.orm import Session
from typing import Optional
from datetime import date
router = APIRouter()

@router.post("/")
def create_torneo_endpoint(nombre:str,fecha_inscripcion:date, competencia:str, session: Session = Depends(get_db)):
    torneo = create_torneo(session,nombre, fecha_inscripcion,competencia)
    if not torneo:
        raise  HTTPException(status_code=404, details="Torneo No encontrado")
    
    return {"Nombre": torneo.nombre,"Fecha_Inscripcion": torneo.fecha_Inscripcion}

@router.get("/{torneo_id}")
def get_torneo_id_endpoint(torneo_id:int, session:Session= Depends(get_db)):
    torneo = get_torneo_id(session,torneo_id)
    return {"id": torneo.id,"nombre":torneo.nombre,"fecha_inscripcion":torneo.fecha_Inscripcion}
    

@router.put("/{torneo_id}")
def update_torneo_id_endpoint(torneo_id:int, nombre:Optional[str],fecha_Inscripcion:Optional[date],competencia:Optional[str], session:Session=Depends(get_db)):
    torneo = update_torneo_id(session,torneo_id,nombre,fecha_Inscripcion,competencia)
    return {"id": torneo.id,"nombre":torneo.nombre,"fecha_inscripcion":torneo.fecha_Inscripcion}

@router.delete("/{torneo_id}")
def delete_torneo_id_endpoint(torneo_id:int, session:Session=Depends(get_db)):
    torneo = delete_torneo_id(session,torneo_id)
    if not torneo:
        raise HTTPException(status_code=404, detail="Torneo no encontrado")
    return {"id": torneo.id,"nombre":torneo.nombre,"fecha_inscripcion":torneo.fecha_Inscripcion}