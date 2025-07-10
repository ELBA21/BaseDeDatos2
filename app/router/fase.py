from fastapi import APIRouter, Depends, HTTPException

from app.models import TorneoCategoria
from ..db import get_db
from ..crud.fase import get_fase_id, create_fase, update_fase, delete_fase

# from ..crud.torneo_categoria import andres.... no hiciste el crud
from sqlalchemy.orm import Session
from typing import Optional

router = APIRouter()


@router.post("/")
def create_fase_endpoint(
    tipo: str, torneo_categoria_id: int, session: Session = Depends(get_db)
):
    tc_id = session.get(
        TorneoCategoria, torneo_categoria_id
    )  # Andres no hicistes el get pipipi
    if tc_id is None:
        raise HTTPException(status_code=404, detail="torneo_categoria no encontrado")

    fase = create_fase(session, tipo, torneo_categoria_id)
    return {
        "id": fase.id,
        "tipo": fase.tipo,
        "torneo_categoria_id": fase.torneo_categoria_id,
    }


@router.get("/{fase_id}")
def get_fase_id_endpoint(fase_id: int, session: Session = Depends(get_db)):
    fase = get_fase_id(session, fase_id)
    if not fase:
        raise HTTPException(status_code=404, detail="Fase no encontrada")
    return {
        "id": fase.id,
        "tipo": fase.tipo,
        "torneo_categoria_id": fase.torneo_categoria_id,
    }


@router.put("/{fase_id}")
def update_fase_endpoint(
    fase_id: int,
    tipo: Optional[str] = None,
    torneo_categoria_id: Optional[int] = None,
    session: Session = Depends(get_db),
):
    if torneo_categoria_id is not None:
        tc_id = session.get(TorneoCategoria, torneo_categoria_id)
        if tc_id is None:
            raise HTTPException(
                status_code=404, detail="torneo_categoria no encontrado"
            )
    fase = update_fase(session, fase_id, tipo, torneo_categoria_id)
    if not fase:
        raise HTTPException(status_code=404, detail="Fase no encontrada")
    return {
        "id": fase.id,
        "tipo": fase.tipo,
        "torneo_categoria_id": fase.torneo_categoria_id,
    }


@router.delete("/{fase_id}")
def delete_fase_endpoint(fase_id: int, session: Session = Depends(get_db)):
    fase = delete_fase(session, fase_id)
    if not fase:
        raise HTTPException(status_code=404, detail="Fase no encontrada")
    return {
        "id": fase.id,
        "tipo": fase.tipo,
        "torneo_categoria_id": fase.torneo_categoria_id,
    }
