
from fastapi import APIRouter, Depends, Request, Response
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud.users import get_user_by_id
from app.utils.session_tokens import get_session_by_id


router = APIRouter(prefix='/api/token', tags=['token'])

class UserResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class Data(BaseModel):
    token: str


@router.post('')
def token(data: Data, db: Session = Depends(get_db)):
    session = get_session_by_id(db, data.token)

    user = get_user_by_id(db, session.user_id)

    return {'verified': True, 'message': 'Session valid', 'user': UserResponse.model_validate(user)}

