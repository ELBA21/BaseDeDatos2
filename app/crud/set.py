from typing import Optional
from sqlalchemy.orm import Session
from ..models import Set

def create_set(session: Session, numero_set:int, puntos_jugador1:int,puntos_jugador2:int, fk_partido):
    sets = Set(numero_Set=numero_set,puntos_Jugador1 = puntos_jugador1, puntos_Jugador2=puntos_jugador2, partido_id = fk_partido)
    session.add(sets)
    session.commit()
    return sets

def get_set_id(session:Session, sets_id:int):
    sets = session.get(Set,sets_id)
    return sets

def update_set_id(session: Session, set_id: int, numero_set:Optional[int],puntos_jugador1:Optional[int], puntos_jugador2:Optional[int],fk_partido:Optional[int]):
    sets= session.get(Set, set_id)
    if not sets:
        print("NO SE ENCONTRO")
        return None
    if numero_set is not None:
        sets.numero_Set = numero_set
    if puntos_jugador1 is not None:
        sets.puntos_Jugador1 = puntos_jugador1
    if puntos_jugador2 is not None:
        sets.puntos_Jugador2 = puntos_jugador2
    if fk_partido is not None:
        sets.partido_id = fk_partido
    session.commit()
    return sets

def delete_set(session: Session, set_id:int):
    sets= session.get(Set, set_id)
    if not sets:
        print("No se ha encontrado")
        return None
    session.delete(sets)
    session.commit()
    return sets