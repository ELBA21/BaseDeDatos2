from datetime import date, datetime, time
from typing import Optional
from sqlalchemy.orm  import Session
from ..models import Partido

def create_partido(session: Session, horario: time, resultado: str):
    partido = Partido(horario = horario, resultado=resultado)
    session.add(partido)
    session.commit()
    return partido