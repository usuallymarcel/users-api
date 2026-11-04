from fastapi import APIRouter, Depends, Response
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.database import get_db


router = APIRouter(prefix='/api/health', tags=['health'])

# Consumers (e.g. pdf-reader) only enable features this list advertises, so a
# new deployment of this API can be rolled out independently of its consumers.
CAPABILITIES = ['session-introspection', 'remember-me']


@router.get('')
def health(response: Response, db: Session = Depends(get_db)):
    try:
        db.execute(text('SELECT 1'))
    except SQLAlchemyError:
        response.status_code = 503
        return {'status': 'unavailable', 'capabilities': []}

    return {'status': 'ok', 'capabilities': CAPABILITIES}
