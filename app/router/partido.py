from fastapi  import APIRouter, Depends, HTTPException
from ..db import get_db
from ..crud.partido import (create_partido)
from sqlalchemy.orm import Session
from typing import Optional
from datetime import date, datetime,time
router = APIRouter()

@router.post("/")
def create_partido_endpoint(horario:time, resultado:str,session: Session = Depends(get_db)):
    partido = create_partido(session, horario, resultado)
    return {"id": partido.id,"date": partido.horario,"resultado": partido.resultado}