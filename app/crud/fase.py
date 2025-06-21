from typing import Optional
from sqlalchemy.orm import Session
from ..models import Fase

def create_fase(session: Session,tipo:str, torneo_id:int):
    if not tipo:
        raise ValueError("El tipo de fase no puede ser nulo o vacío.")
    if not torneo_id:
        raise ValueError("El ID del torneo no puede ser nulo o vacío.")
    fase = Fase(tipo=tipo, Torneo_id=torneo_id)
    session.add(fase)
    session.commit()
    return fase

def get_fase_id(session: Session, fase_id: int):
    fase = session.get(Fase, fase_id)
    if not fase:
        raise ValueError("Fase no encontrada.")
    return fase

def update_fase_id(session: Session, fase_id: int, tipo: Optional[str] = None, torneo_id: Optional[int] = None):
    fase = session.get(Fase, fase_id)
    if not fase:
        raise ValueError("Fase no encontrada.")
    
    if tipo is not None:
        fase.tipo = tipo
    if torneo_id is not None:
        fase.Torneo_id = torneo_id
    
    session.commit()
    return fase

def delete_fase(session: Session, fase_id: int):
    fase = session.get(Fase, fase_id)
    if not fase:
        raise ValueError("Fase no encontrada.")
    
    session.delete(fase)
    session.commit()
    return fase