from typing import Optional
from sqlalchemy.orm import Session
from ..models import Fase, TorneoCategoria

def create_fase(session: Session,tipo:str,torneo_categoria_id: int):
    if not tipo:
        raise ValueError("El tipo de fase no puede ser nulo o vacío.")
    if not session.get(TorneoCategoria, torneo_categoria_id):
        raise ValueError("El torneo_categoria_id proporcionado no existe.")
    fase = Fase(tipo=tipo, torneo_categoria_id=torneo_categoria_id)
    session.add(fase)
    session.commit()
    return fase

def get_fase_id(session: Session, fase_id: int):
    fase = session.get(Fase, fase_id)
    if not fase:
        raise ValueError("Fase no encontrada.")
    return fase

def update_fase_id(session: Session, fase_id: int, tipo: Optional[str] = None, torneo_categoria_id: Optional[int] = None):
    fase = session.get(Fase, fase_id)
    if not fase:
        raise ValueError("Fase no encontrada.")
    
    if tipo is not None:
        fase.tipo = tipo

    if torneo_categoria_id is not None:
        if not session.get(TorneoCategoria, torneo_categoria_id):
            raise ValueError("torneo_categoria_id no existe.")
        fase.torneo_categoria_id = torneo_categoria_id
    
    session.commit()
    return fase

def delete_fase(session: Session, fase_id: int):
    fase = session.get(Fase, fase_id)
    if not fase:
        raise ValueError("Fase no encontrada.")
    
    session.delete(fase)
    session.commit()
    return fase