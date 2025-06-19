from datetime import date
from typing import Optional
from sqlalchemy.orm import Session
from ..models import Jugador, Asociacion,Categoria

def create_jugador(session: Session,nombre:str, fecha_naciemiento: date,categoria: Categoria, asociacion: Optional[Asociacion]=None):
    jugador= Jugador(nombre= nombre,fecha_naciemiento= fecha_naciemiento, asociacion= asociacion, categoria= categoria)
    Session.add(jugador)
    Session.commit()
    return jugador

def get_jugadores_all(session: Session):
    return Session.query(Jugador).all()

def update_jugador_nombre(session:Session,jugador_id:int, nombre:str):
    jugador = Session.get(Jugador, jugador_id)
    if not jugador:
        print("NO ENCONTRADO")
        return None
    jugador.nombre= nombre
    session.commit()
    return jugador

