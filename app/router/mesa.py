from fastapi  import APIRouter, Depends, HTTPException
from ..db import get_db
from ..crud.mesa import (get_mesa_id, create_mesa, update_mesa_id, delete_mesa)
from sqlalchemy.orm import Session
from typing import Optional
router = APIRouter()

@router.post("/")
def create_mesa_endpoint(torneo_id: int, session: Session = Depends(get_db)):
    mesa = create_mesa(session, torneo_id)
    return {"id": mesa.id, "torneo_id": mesa.torneo_id}

@router.get("/{mesa_id}")
def get_mesa_id_endpoint(mesa_id: int, session: Session = Depends(get_db)):
    mesa = get_mesa_id(session, mesa_id)
    if not mesa:
        raise HTTPException(status_code=404, detail="Mesa no encontrada")
    return {"id": mesa.id, "torneo_id": mesa.torneo_id}

@router.put("/{mesa_id}")
def update_mesa_id_endpoint(mesa_id: int, torneo_id: Optional[int] = None, session: Session = Depends(get_db)):
    mesa = update_mesa_id(session, mesa_id, torneo_id)
    if not mesa:
        raise HTTPException(status_code=404, detail="Mesa no encontrada")
    return {"id": mesa.id, "torneo_id": mesa.torneo_id}

@router.delete("/{mesa_id}")
def delete_mesa_endpoint(mesa_id: int, session: Session = Depends(get_db)):
    mesa = delete_mesa(session, mesa_id)
    if not mesa:
        raise HTTPException(status_code=404, detail="Mesa no encontrada")
    return {"id": mesa.id, "torneo_id": mesa.torneo_id}