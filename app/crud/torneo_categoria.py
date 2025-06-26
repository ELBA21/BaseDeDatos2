from typing import Optional
from sqlalchemy.orm import Session
from ..models import TorneoCategoria, Torneo, Categoria

###ESTE LO ISE YO COPIANDOLE AL BENJA, EL OTRO LO ISO SHATYEPETE

# def create_torneo_categoria(session: Session, torneo_id: int, categoria_id: int):
#     torneo_categoria = TorneoCategoria(torneo_id = torneo_id, categoria_id = categoria_id)
#     session.add(torneo_categoria)
    # session.commit()
#     return torneo_categoria

# def create_torneo_categoria(session: Session, torneo_id: int, categoria_id: int):
#     existe = session.query(TorneoCategoria).filter_by(
#         torneo_id=torneo_id, categoria_id=categoria_id
#     ).first()
    
#     if existe:
#         return existe  # o lanzar un error si no quieres duplicados

#     nueva = TorneoCategoria(torneo_id=torneo_id, categoria_id=categoria_id)
#     session.add(nueva)
#     session.commit()
#     return nueva

def create_torneo_categoria(session: Session, torneo_id: int, categoria_id: int):
    # Validar que el torneo existe
    torneo = session.query(Torneo).get(torneo_id)
    if not torneo:
        raise ValueError(f"Torneo con ID {torneo_id} no existe")

    # Validar que la categoría existe
    categoria = session.query(Categoria).get(categoria_id)
    if not categoria:
        raise ValueError(f"Categoría con ID {categoria_id} no existe")

    # Verificar si la relación ya existe
    existe = session.query(TorneoCategoria).filter_by(
        torneo_id=torneo_id, categoria_id=categoria_id
    ).first()

    if existe:
        return existe  # o lanzar un error si no quieres duplicados

    nueva = TorneoCategoria(torneo_id=torneo_id, categoria_id=categoria_id)
    session.add(nueva)
    session.commit()
    return nueva

