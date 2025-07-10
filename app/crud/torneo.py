from datetime import date, timedelta
from typing import Optional
from sqlalchemy.orm import Session
from ..models import Torneo

def create_torneo(session: Session,nombre:str, fecha_Inscripcion:date, competencia:Optional[str] = None):
    hoy = date.today()
    limite = hoy + timedelta(days=30)
    if (hoy > fecha_Inscripcion or fecha_Inscripcion > limite):
        raise ValueError("La fecha de inscripción debe estar dentro de los próximos 30 días.")
    torneo = Torneo(nombre=nombre, fecha_inscripcion=fecha_Inscripcion, competencia = competencia)

    session.add(torneo)
    session.commit()
    return torneo

def get_torneo_id(session:Session,torneo_id:int):
    torneo = session.get(Torneo, torneo_id)
    if not torneo:
        raise ValueError("Torneo no encontrado")
    return torneo    

def update_torneo_id(session:Session, torneo_id:int, nombre:Optional[str] = None,fecha_Inscripcion:Optional[date] = None,competencia:Optional[str] = None):
    torneo = session.get(Torneo, torneo_id)
    hoy = torneo.fecha_Inscripcion
    limite = hoy + timedelta(days=7)

    if not torneo:
        raise ValueError("Torneo no encontrado")
    if nombre is not None:
        torneo.nombre = nombre
    if fecha_Inscripcion is not None:
        if (hoy > fecha_Inscripcion or fecha_Inscripcion > limite):
            raise ValueError("No puedes correr la inscripción más de 7 días")
        torneo.fecha_Inscripcion = fecha_Inscripcion
    if competencia is not None:
        torneo.competencia = competencia
    session.commit()
    return torneo

def delete_torneo_id(session:Session, torneo_id: int):
    torneo = session.get(Torneo, torneo_id)
    if not torneo:
        raise ValueError("Torneo no encontrado")
    session.delete(torneo)
    session.commit()