from fastapi  import APIRouter, Depends, HTTPException
from ..db import get_db
from ..crud.set import (get_set_id, create_set, update_set_id, delete_set)
from sqlalchemy.orm import Session
from typing import Optional
router = APIRouter()

@router.post("/")
def create_set_endpoint(numero_sets:int, puntos_jugador1:int,puntosjugador2:int, fk_partido:int, session: Session = Depends(get_db)):
    el_set = create_set(session,numero_sets,puntos_jugador1,puntosjugador2,fk_partido)
    return {"numero_Set": el_set.numero_Set,"puntos Jugador1": el_set.puntos_Jugador1,"puntos Jugador2": el_set.puntos_Jugador2}

@router.get("/{set_id}")
def get_set_id_endpoint(set_id:int,session: Session = Depends(get_db)):
    el_set = get_set_id(session,set_id)
    if not el_set:
        raise HTTPException(status_code=404, detail="Set No Encontrado")
    return {"id": el_set.id,"id_partido" :el_set.partido_id}
    

@router.put("/{set_id}")
def update_sets_id_endpoint(set_id:int, numero_set:Optional[int], puntos_jugador1:Optional[int]=None, puntos_jugador2:Optional[int]=None,fk_partido:Optional[int]=None, session:Session = Depends(get_db)):
    el_set=  update_set_id(session, set_id,numero_set,puntos_jugador1,puntos_jugador2,fk_partido)
    if not el_set:
        raise HTTPException(status_code=404,details="Set no encontrado")
    return {"id": el_set.id,"numero_set": el_set.numero_Set,"puntos_jugador1": el_set.puntos_Jugador1,"puntos_jugador2": el_set.puntos_Jugador2}

@router.delete("/{set_id}")
def delete_set_endpoint(set_id:int, session:Session=Depends(get_db)):
    el_set = delete_set(session, set_id)
    if not el_set:
        raise HTTPException(error_code=404,details="Set No encontrado")
    return {"id": el_set.id,"numero set": el_set.numero_Set,"puntos jugador 1": el_set.puntos_Jugador1, "puntos jugador 2": el_set.puntos_Jugador2}