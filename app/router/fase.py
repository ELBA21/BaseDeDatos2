from fastapi  import APIRouter, Depends, HTTPException
from ..db import get_db
from ..crud.fase import (get_fase_id, create_fase, update_fase_id, delete_fase)
from sqlalchemy.orm import Session
from typing import Optional
router = APIRouter()

@router.post("/")
def create_fase_endpoint(tipo: str, torneo_id: int, session: Session = Depends(get_db)):
    fase = create_fase(session, tipo, torneo_id)
    return {"id": fase.id, "tipo": fase.tipo, "torneo_id": fase.Torneo_id}


@router.get("/{fase_id}")
def get_fase_id_endpoint(fase_id: int, session: Session = Depends(get_db)):
    fase = get_fase_id(session, fase_id)
    if not fase:
        raise HTTPException(status_code=404, detail="Fase no encontrada")
    return {"id": fase.id, "tipo": fase.tipo, "torneo_id": fase.Torneo_id}

@router.put("/{fase_id}")
def update_fase_id_endpoint(fase_id: int, tipo: Optional[str] = None, torneo_id: Optional[int] = None, session: Session = Depends(get_db)):
    fase = update_fase_id(session, fase_id, tipo, torneo_id)
    if not fase:
        raise HTTPException(status_code=404, detail="Fase no encontrada")
    return {"id": fase.id, "tipo": fase.tipo, "torneo_id": fase.Torneo_id}
@router.delete("/{fase_id}")
def delete_fase_endpoint(fase_id: int, session: Session = Depends(get_db)):
    fase = delete_fase(session, fase_id)
    if not fase:
        raise HTTPException(status_code=404, detail="Fase no encontrada")
    return {"id": fase.id, "tipo": fase.tipo, "torneo_id": fase.Torneo_id}