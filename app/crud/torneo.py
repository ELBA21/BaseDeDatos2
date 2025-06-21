from datetime import date
from typing import Optional
from sqlalchemy.orm import Session
from ..models import Torneo

def create_torneo(session: Session,nombre:Optional[str],fecha_Inscripcion:Optional[date],competencia:Optional[str]):
    torneo = Torneo(nombre= nombre,fecha_Inscripcion=fecha_Inscripcion, competencia = competencia)
    session.add(torneo)
    session.commit()
    return torneo

def get_torneo_id(session:Session,torneo_id:int):
    torneo = session.get(Torneo, torneo_id)
    if not torneo:
        print("No se encontro")
    return torneo    

def update_torneo_id(session:Session, torneo_id:int, nombre:Optional[str],fecha_Inscripcion:Optional[date],competencia:Optional[str]):
    torneo = session.get(Torneo, torneo_id)
    if not torneo:
        print("No encontrado")
        return None
    if nombre is not None:
        torneo.nombre = nombre
    if fecha_Inscripcion is not None:
        torneo.fecha_Inscripcion= fecha_Inscripcion
    if competencia is not None:
        torneo.competencia = competencia
    session.commit()
    return torneo

def delete_torneo_id(session:Session, torneo_id: int):
    torneo = session.get(Torneo, torneo_id)
    if not torneo:
        print("No encontrado")
        return None
    session.delete(torneo)
    session.commit()
    return torneo