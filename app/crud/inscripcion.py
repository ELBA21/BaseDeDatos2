from typing import Optional
from sqlalchemy.orm import Session
from ..models import Inscripcion, Jugador, Equipo, TorneoCategoria

###ESTE LO ISE YO COPIANDOME AMI MISMO OWO AWA EWE, AWA QUE PARECE EWE PERO SABE A UWU


def create_inscripcion(
    session: Session,
    torneo_categoria_id: int,
    jugador_id: Optional[int] = None,
    equipo_id: Optional[int] = None,
):
    # Validar que el jugador existe
    if jugador_id is not None and equipo_id is not None:
        # hacer que no se puedan inscribir juntos >:(
        raise ValueError(
            f"No se pueden inscribir jugadores y equipos en el mismo torneo"
        )

    if jugador_id is None:
        equipo = session.query(Equipo).get(equipo_id)
        if not equipo:
            raise ValueError(f"Equipo con ID {equipo_id} no existe")

    if equipo_id is None:
        jugador = session.query(Jugador).get(jugador_id)
        if not jugador:
            raise ValueError(f"Jugador con ID {jugador_id} no existe")

    # Validar que la equipo existe

    torneo_categoria = session.query(TorneoCategoria).get(torneo_categoria_id)
    if not torneo_categoria:
        raise ValueError(f"TorneoCategoria con ID {torneo_categoria_id} no existe")

    # Verificar si la relación ya existe
    existe = (
        session.query(Inscripcion)
        .filter_by(
            jugador_id=jugador_id,
            equipo_id=equipo_id,
            torneo_categoria_id=torneo_categoria_id,
        )
        .first()
    )

    if existe:
        raise ValueError(f"El equipo o el jugador ya estan inscritos")

    nueva = Inscripcion(
        jugador_id=jugador_id,
        equipo_id=equipo_id,
        torneo_categoria_id=torneo_categoria_id,
    )
    session.add(nueva)
    session.commit()
    return nueva


# grasias andres
def get_inscripcion_id(session: Session, inscripcion_id: int):
    inscripcion = session.get(Inscripcion, inscripcion_id)
    return inscripcion


def update_inscripcion_id(
    session: Session,
    inscripcion_id: int,
    torneo_categoria_id: Optional[int] = None,
    jugador_id: Optional[int] = None,
    equipo_id: Optional[int] = None,
):
    inscripcion = session.get(Inscripcion, inscripcion_id)
    if not inscripcion:
        raise ValueError(f"Inscripcion no encontrada")
    if torneo_categoria_id is not None:
        inscripcion.torneo_categoria_id = torneo_categoria_id
    if (
        inscripcion.jugador_id is None and equipo_id is not None
    ):  # asegurandonos de no editar si es que uno de los campos esta vacio
        inscripcion.equipo_id = equipo_id
    elif inscripcion.equipo_id is None and jugador_id is not None:
        inscripcion.jugador_id = jugador_id
    session.commit()
    return inscripcion


def delete_inscripcion(session: Session, inscripcion_id: int):
    inscripcion = session.get(Inscripcion, inscripcion_id)
    if not Inscripcion:
        raise ValueError("inscripcion no encontrada")
    session.delete(inscripcion)
    session.commit()
    return inscripcion

