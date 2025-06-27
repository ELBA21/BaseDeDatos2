from fastapi  import APIRouter, Depends, HTTPException
from ..db import get_db
from ..crud.inscripcion import create_inscripcion
from sqlalchemy.orm import Session
from typing import Optional
router = APIRouter()


@router.post("/")
def create_inscripcion_endpoint(torneo_categoria_id: int, jugador_id: Optional[int] = None, equipo_id: Optional[int] = None, session: Session = Depends(get_db)):
    if((jugador_id == None and equipo_id==None) or (jugador_id != None and equipo_id!=None)):
        raise HTTPException(status_code=400, detail="Solo se puede inscribir un equipo o un jugador a la vez")

    if((jugador_id != None and jugador_id<1) or (equipo_id != None and equipo_id<1) or torneo_categoria_id<1):
        raise HTTPException(status_code=400, detail="Necesito un entero positivo, amermelao")
    
    inscripcion = create_inscripcion(session, torneo_categoria_id, jugador_id, equipo_id)
    return {"id": inscripcion.id, "jugador_id": inscripcion.jugador_id, "equipo_id": inscripcion.equipo_id, "torneo_categoria_id": inscripcion.torneo_categoria_id}