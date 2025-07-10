from fastapi  import APIRouter, Depends, HTTPException
from ..db import get_db
from ..crud.categoria import (get_categoria_id, create_categoria, update_categoria_id, delete_categoria)
from sqlalchemy.orm import Session
from typing import Optional
router = APIRouter()


@router.post("/")
def create_categoria_endpoint(edad_Min:int, edad_Max:int, genero:str, set_por_partido:int, puntos_por_set:int, session: Session = Depends(get_db)):
    categoria = create_categoria(session, edad_Min, edad_Max, genero, set_por_partido, puntos_por_set)
    return {
        "id": categoria.id,
        "edad_Min": categoria.edad_Min,
        "edad_Max": categoria.edad_Max,
        "genero": categoria.genero,
        "set_por_partido": categoria.set_por_partido,
        "puntos_por_set": categoria.puntos_por_set
    }

@router.get("/{categoria_id}")
def get_categoria_id_endpoint(categoria_id:int, session: Session =Depends(get_db)):
    categoria = get_categoria_id(session, categoria_id)
    return {
        "id": categoria.id,
        "edad_Min": categoria.edad_Min,
        "edad_Max": categoria.edad_Max,
        "genero": categoria.genero,
        "set_por_partido": categoria.set_por_partido,
        "puntos_por_set": categoria.puntos_por_set
    }

@router.put("/{categoria_id}")
def update_categoria_id_endpoint(categoria_id:int, edad_Min:Optional[int]=None, edad_Max:Optional[int]=None, genero:Optional[str]=None, set_por_partido:Optional[int]=None, puntos_por_set:Optional[int]=None, session: Session = Depends(get_db)):
    categoria = update_categoria_id(session, categoria_id, edad_Min, edad_Max, genero, set_por_partido, puntos_por_set)
    return {
        "id": categoria.id,
        "edad_Min": categoria.edad_Min,
        "edad_Max": categoria.edad_Max,
        "genero": categoria.genero,
        "set_por_partido": categoria.set_por_partido,
        "puntos_por_set": categoria.puntos_por_set
    }

@router.delete("/{categoria_id}")
def delete_categoria_endpoint(categoria_id:int, session: Session = Depends(get_db)):
    categoria = delete_categoria(session, categoria_id)
    return {"detail": f"Categoria con id {categoria.id} eliminada correctamente"}