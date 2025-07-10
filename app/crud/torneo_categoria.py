from typing import Optional
from sqlalchemy.orm import Session
from ..models import TorneoCategoria, Torneo, Categoria

def create_torneo_categoria(session: Session, torneo_id: int, categoria_id: int):
    # Validar que el torneo existe
    torneo = session.get(Torneo, torneo_id)
    if not torneo:
        raise ValueError(f"Torneo con ID {torneo_id} no existe")

    # Validar que la categoría existe
    categoria = session.get(Categoria, categoria_id)
    if not categoria:
        raise ValueError(f"Categoría con ID {categoria_id} no existe")

    # Verificar si la relación ya existe
    existe = session.query(TorneoCategoria).filter_by(
        torneo_id=torneo_id, categoria_id=categoria_id
    ).first()

    if existe:
        raise ValueError("La relación ya existe")

    torneo_categoria = TorneoCategoria(torneo_id=torneo_id, categoria_id=categoria_id)
    session.add(torneo_categoria)
    session.commit()
    return torneo_categoria

def get_torneo_categoria_id(session:Session,torneo_categoria_id:int):
    torneo_categoria = session.get(Torneo, torneo_categoria_id)
    if not torneo_categoria:
        raise ValueError("Relación Torneo-Categoría no encontrada")
    return torneo_categoria    

def delete_torneo_categoria_id(session:Session, torneo_categoria_id: int):
    torneo_categoria = session.get(Torneo, torneo_categoria_id)
    if not torneo_categoria:
        raise ValueError("Relación Torneo-Categoría no encontrado")
    session.delete(torneo_categoria)
    session.commit()

