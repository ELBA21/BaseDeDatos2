from datetime import date
from typing import Optional
from sqlalchemy.orm import Session
from ..models import Jugador, Asociacion, Categoria, Genero, Ciudad


def create_jugador(
    session: Session,
    nombre: str,
    fecha_nacimiento: date,
    genero: int,
    ciudad: int,
    categoria_id: int,
    asociacion_id: Optional[int],
):
    today = date.today()
    if fecha_nacimiento < today:
        jugador = Jugador(
            nombre=nombre,
            fecha_nacimiento=fecha_nacimiento,
            genero=genero,
            ciudad=ciudad,
            asociacion_id=asociacion_id,
            categoria_id=categoria_id,
        )
        session.add(jugador)
        session.commit()
        return jugador
    else:
        print("No se admiten paradojas temporales")


def get_jugador_id(session: Session, jugador_id: int):
    jugador = session.get(Jugador, jugador_id)
    return jugador


def update_jugador_id(
    session: Session,
    jugador_id: int,
    nombre: Optional[str] = None,
    fecha_nacimiento: Optional[date] = None,
    genero: Optional[int] = None,
    # pais: Optional[str] = None,
    ciudad: Optional[int] = None,
    asociacion_id: Optional[int] = None,
    categoria_id: Optional[int] = None,
):
    jugador = session.get(Jugador, jugador_id)
    if not jugador:
        print("NO ENCONTRADO")
        return None
    if nombre is not None:
        jugador.nombre = nombre
    today = date.today()
    if fecha_nacimiento is not None:
        if fecha_nacimiento < today:
            jugador.fecha_nacimiento = fecha_nacimiento
        else:
            print("No se admiten viajeros en el tiempo")
    if (
        genero is not None
    ):  # hay que ser progresivos, que pasa si alguien no tiene genero, lo dejare asi porque demas que el profe dice q no,
        # pero weno los generos paises y ciudades deberian ser tablas apartes mis amigos programadores y benjamin martinez,
        # se que nadie va a leer esto
        jugador.genero = genero
    if pais is not None:
        jugador.pais = pais
    if ciudad is not None:
        jugador.ciudad = ciudad
    # if asociacion_id is not None:  # un jugador si puede tener None en categoria
    jugador.asociacion_id = asociacion_id
    if categoria_id is not None:
        jugador.categoria_id = categoria_id
    session.commit()
    return jugador


def delete_jugador(session: Session, jugador_id: int):
    jugador = session.get(Jugador, jugador_id)
    if not jugador:
        print("NO ENCONTRADO")
        return None
    session.delete(jugador)
    session.commit()
    return jugador
