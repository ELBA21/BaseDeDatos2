from fastapi  import APIRouter, Depends, HTTPException
from ..db import get_db
from ..crud.asociacion import create_torneo_categoria
from sqlalchemy.orm import Session
from typing import Optional
router = APIRouter()


@router.post("/")
def create_torneo_categoria_endpoint(torneo_id: int, categoria_id: int, session: Session = Depends(get_db)):
    torneo_categoria = create_torneo_categoria(session, torneo_id, categoria_id)
    return {"torneo_id": torneo_categoria.torneo_id, "categoria_id": torneo_categoria.categoria_id}