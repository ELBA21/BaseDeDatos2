from typing import Optional
from sqlalchemy.orm import Session
from ..models import Jugador, Asociacion,Categoria

def create_asociacion(session: Session, nombre: str, ciudad: str, pais: str):
    asociacion = Asociacion(nombre=nombre, ciudad=ciudad, pais=pais)
    session.add(asociacion)
    session.commit()
    return asociacion

def get_asociacion_all(session: Session):
    return session.query(Asociacion).all()

def update_asociacion_all(session: Session, asociacion_id: int, nombre: Optional[str] = None, ciudad: Optional[str] = None, pais: Optional[str] = None):
    asociacion = session.get(Asociacion, asociacion_id)
    if not asociacion:
        print("NO ENCONTRADO")
        return None
    if nombre is not None:
        asociacion.nombre = nombre
    if ciudad is not None:
        asociacion.ciudad = ciudad
    if pais is not None:
        asociacion.pais = pais
    session.commit()
    return asociacion

def delete_asociacion(session: Session, asociacion_id: int):
    asociacion = session.get(Asociacion, asociacion_id)
    if not asociacion:
        print("NO ENCONTRADO")
        return None
    session.delete(asociacion)
    session.commit()
    return asociacion    

