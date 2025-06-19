from fastapi  import APIRouter, Depends, HTTPException
from ..db import get_db
from ..crud.jugador import (get_jugador_all, get_jugador_by_id, create_jugador, update_jugador_nombre, update_jugador_fechaNacimiento, update_jugador_genero, update_jugador_pais, update_jugador_ciudad, update_jugador_asociacion, update_jugador_categoria, delete_jugador)
from sqlalchemy.orm import Session
router = APIRouter()



@router.get("/")
def get_jugadores_all_endpoint(session: Session = Depends(get_db)):
    jugadores = get_jugador_all(session)
    return [{"id": jugador.id } for jugador in jugadores]
