from typing import Optional
from sqlalchemy.orm import Session
from ..models import Categoria
from fastapi import HTTPException

def create_categoria(session: Session, edad_Min: int, edad_Max: int, set_por_partido: int, puntos_por_set:int, genero: int):
    if not (0 < edad_Min <= edad_Max):
        raise HTTPException(status_code=400, detail="edad_Min debe ser menor que edad_Max y ambos deben ser positivos.")
    if not 0<genero<3:
        raise HTTPException(status_code=400, detail="Solo se puede masculino [1] o femenino [2] por ahora")
    if set_por_partido <= 0:
        raise HTTPException(status_code=400, detail="set_por_partido debe ser un número positivo.")
    if puntos_por_set <= 0:
        raise HTTPException(status_code=400, detail="puntos_por_set debe ser un número positivo.")
    categoria = Categoria(edad_Min=edad_Min, edad_Max=edad_Max, set_por_partido=set_por_partido, puntos_por_set=puntos_por_set, genero=genero)
    session.add(categoria)
    session.commit()
    return categoria

def get_categoria_id(session: Session, categoria_id: int):
    categoria = session.get(Categoria, categoria_id)
    if not categoria:
        raise HTTPException(status_code=400, detail="Categoria no encontrada")
    return categoria

def update_categoria_id(session: Session, categoria_id: int, edad_Min: Optional[int] = None, edad_Max: Optional[int] = None, set_por_partido: Optional[int] = None, puntos_por_set: Optional[int] = None,  genero: Optional[int] = None,):
    categoria = session.get(Categoria, categoria_id)
    if not categoria:
        raise HTTPException(status_code=400, detail="Categoria no encontrada")
    if edad_Min is not None:
        if edad_Min <= 0:
            raise HTTPException(status_code=400, detail="edad_Min debe ser un número positivo.")
        if (edad_Max is not None and edad_Min > edad_Max) or (categoria.edad_Max < edad_Min):
            raise HTTPException(status_code=400, detail="edad_Min debe ser menor o igual que edad_Max.")
        categoria.edad_Min = edad_Min
    if edad_Max is not None:
        if edad_Max <= 0:
            raise HTTPException(status_code=400, detail="edad_Max debe ser un número positivo.")
        if (edad_Min is not None and edad_Max < edad_Min) or (edad_Max < categoria.edad_Min):
            raise HTTPException(status_code=400, detail="edad_Max debe ser mayor o igual que edad_Min.")
        categoria.edad_Max = edad_Max
    if genero is not None:
        if not 0<genero<3:
            raise HTTPException(status_code=400, detail="Solo se puede masculino [1] o femenino [2] por ahora")
        categoria.genero = genero
    if set_por_partido is not None:
        if set_por_partido <= 0:
            raise HTTPException(status_code=400, detail="set_por_partido debe ser un número positivo.")
        categoria.set_por_partido = set_por_partido
    if puntos_por_set is not None:
        if puntos_por_set <= 0:
            raise HTTPException(status_code=400, detail="puntos_por_set debe ser un número positivo.")
        categoria.puntos_por_set = puntos_por_set
    session.commit()
    return categoria

def delete_categoria(session: Session, categoria_id: int):
    categoria = session.get(Categoria, categoria_id)
    if not categoria:
        raise HTTPException(status_code=400, detail="Categoria no encontrada")
    session.delete(categoria)
    session.commit()
    return categoria

