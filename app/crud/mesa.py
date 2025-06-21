from typing import Optional
from sqlalchemy.orm import Session
from ..models import Mesa

def create_mesa(session: Session, torneo_id:int):
    mesa = Mesa(Torneo_id=torneo_id)
    session.add(mesa)
    session.commit()
    return mesa

def get_mesa_id(session: Session, mesa_id: int):
    if not mesa_id:
        print("ID de mesa no proporcionado")
        return None
    mesa = session.get(Mesa, mesa_id)
    if not mesa:
        print("Mesa no encontrada")
    return mesa

def update_mesa_id(session: Session, mesa_id: int, torneo_id: Optional[int] = None):
    mesa = session.get(Mesa, mesa_id)
    if not mesa:
        print("Mesa no encontrada")
        return None
    if torneo_id is not None:
        mesa.Torneo_id = torneo_id
    else:
        print("No se ha insertado torneo_id")
    session.commit()
    return mesa

def delete_mesa(session: Session, mesa_id: int):
    mesa = session.get(Mesa, mesa_id)
    if not mesa:
        print("Mesa no encontrada")
        return None
    session.delete(mesa)
    session.commit()
    return mesa