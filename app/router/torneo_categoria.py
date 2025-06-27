from fastapi  import APIRouter, Depends, HTTPException
from ..db import get_db
from ..crud.torneo_categoria import create_torneo_categoria
from sqlalchemy.orm import Session
from typing import Optional
router = APIRouter()


@router.post("/")
def create_torneo_categoria_endpoint(torneo_id: int, categoria_id: int, session: Session = Depends(get_db)):
    if(torneo_id<1 or categoria_id<1):
        raise HTTPException(status_code=400, detail="Necesito un entero positivo, amermelao")
    torneo_categoria = create_torneo_categoria(session, torneo_id, categoria_id)
    return {"id": torneo_categoria.id, "torneo_id": torneo_categoria.torneo_id, "categoria_id": torneo_categoria.categoria_id}