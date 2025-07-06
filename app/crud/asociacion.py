from typing import Optional
from sqlalchemy.orm import Session
from ..models import Asociacion


def create_asociacion(session: Session, nombre: str, ciudad: int):
    asociacion = Asociacion(nombre=nombre, ciudad=ciudad)
    session.add(asociacion)
    session.commit()
    return asociacion


def get_asociacion_id(session: Session, asociacion_id: int):
    if not asociacion_id:
        print("ID no proporcionado")
        return None
    asociacion = session.get(Asociacion, asociacion_id)
    if not asociacion:
        print("Asociacion no encontrada")
        return None
    return asociacion


def update_asociacion_id(
    session: Session,
    asociacion_id: int,
    nombre: Optional[str] = None,
    ciudad: Optional[str] = None,
):
    asociacion = session.get(Asociacion, asociacion_id)
    if not asociacion:
        print("NO ENCONTRADO")
        return None
    if nombre is not None:
        asociacion.nombre = nombre
    else:
        print("No se insserto nombre")
    if ciudad is not None:
        asociacion.ciudad = ciudad
    else:
        print("No se ha insertado ciudad")
    # if pais is not None:
    #    asociacion.pais = pais
    # else:
    #    print("No se ha insertado pais")
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
