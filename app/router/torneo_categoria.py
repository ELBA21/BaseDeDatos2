from fastapi  import APIRouter, Depends, HTTPException
from ..db import get_db
from ..crud.torneo_categoria import create_torneo_categoria, get_torneo_categoria_id, delete_torneo_categoria_id
from sqlalchemy.orm import Session
from typing import Optional
router = APIRouter()


@router.post("/")
def create_torneo_categoria_endpoint(torneo_id: int, categoria_id: int, session: Session = Depends(get_db)):
    if(torneo_id<1 or categoria_id<1):
        raise HTTPException(status_code=400, detail="Necesito un entero positivo, amermelao")
    torneo_categoria = create_torneo_categoria(session, torneo_id, categoria_id)
    return {"id": torneo_categoria.id, "torneo_id": torneo_categoria.torneo_id, "categoria_id": torneo_categoria.categoria_id}

@router.get("/{torneo_categoria_id}")
def get_torneo_categoria_id_endpoint(torneo_categoria_id: int, session:Session= Depends(get_db)):
    torneo_categoria = get_torneo_categoria_id(session, torneo_categoria_id)
    return {"id": torneo_categoria.id, "torneo_id": torneo_categoria.torneo_id, "categoria_id": torneo_categoria.categoria_id}

@router.delete("/{torneo_categoria_id}")
def delete_torneo_categoria_id_endpoint(torneo_categoria_id:int, session:Session=Depends(get_db)):
    delete_torneo_categoria_id(session, torneo_categoria_id)